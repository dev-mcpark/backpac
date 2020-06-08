import re

from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from app.models import Member, Order


def regex_exists(pattern, value):
    p = re.compile(pattern)
    m = p.search(value)

    if m:
        return True
    return False


class MyRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True)
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
            raise serializers.ValidationError(
                "Contains one or more English uppercase letters, lowercase English letters, special characters, and numbers"
            )
        return password

    def validate_phone(self, phone):
        # 숫자만 허용
        if regex_exists('[^0-9]+', phone):
            raise serializers.ValidationError("Only numbers are allowed")

        return phone


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        order = Order.objects.filter(user=instance).last()
        res['last_order'] = OrderSerializer(order).data
        return res
