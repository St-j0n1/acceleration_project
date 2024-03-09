from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password', 'confirm_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            return serializers.ValidationError('Password does not match')
        return attrs

    def create(self, validated_data):
        _ = validated_data.pop('confirm_password')
        new_user = User.objects.create_user(**validated_data)
        new_user.save()
        return new_user

    def to_representation(self, instance):
        return {'message': 'success'}