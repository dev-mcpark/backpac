from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from app.models import Member, Order


class MyRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True)
    nickname = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    gender = serializers.ChoiceField(choices=['M', 'F'], required=False)

    def validate_username(self, username):
        # TODO 한글, 영문 대소문자만 허용

        return username

    def validate_nickname(self, nickname):
        # TODO 영문 소문자만 허용
        return nickname

    def validate_password1(self, password):
        # TODO 영문 대문자, 영문 소문자, 특수 문자, 숫자 각 1개 이상씩 포함
        return password

    def validate_phone(self, phone):
        # TODO 숫자
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
