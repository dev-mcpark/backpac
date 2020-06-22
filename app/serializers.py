from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from app.models import Member, Order
from app.utils import regex_exists


class MyRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    nickname = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=['M', 'F'], required=False)

    def validate_username(self, username):
        # 한글, 영문 대소문자만 허용
        if regex_exists('[^ㄱ-ㅣ가-힣a-zA-Z]+', username):
            raise serializers.ValidationError("Only Korean and English uppercase and lowercase letters are allowed")
        return username

    def validate_nickname(self, nickname):
        # 영문 소문자만 허용
        if regex_exists('[^a-z]+', nickname):
            raise serializers.ValidationError("Only lower case letters are allowed")
        return nickname

    def validate_password1(self, password):
        # 영문 대문자, 영문 소문자, 특수 문자, 숫자 각 1개 이상씩 포함
        if regex_exists('[a-z]+', password) and \
                regex_exists('[A-Z]+', password) and \
                regex_exists('[0-9]+', password) and \
                regex_exists('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', password):
            return password
        else:
            raise serializers.ValidationError(
                "Contains one or more English uppercase letters, lowercase English letters, special characters, and numbers"
            )

    def validate_phone(self, phone):
        # 숫자만 허용
        if regex_exists('[^0-9]+', phone):
            raise serializers.ValidationError("Only numbers are allowed")

        return phone

    def custom_signup(self, request, user):
        user.nickname = self.cleaned_data.get('nickname')
        user.phone = self.cleaned_data.get('phone')
        user.gender = self.cleaned_data.get('gender')
        user.save()

    def get_cleaned_data(self):
        return {
            'nickname': self.validated_data.get('nickname', ''),
            'phone': self.validated_data.get('phone', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'gender': self.validated_data.get('gender', ''),
        }


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'order_number': {'read_only': True},
            'product': {'write_only': True},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'email', 'username', 'nickname', 'phone', 'gender']

    def to_representation(self, instance):
        res = super().to_representation(instance)
        order = Order.objects.filter(user=instance).last()
        res['last_order'] = OrderSerializer(order).data
        return res
