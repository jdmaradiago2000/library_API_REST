from rest_framework import serializers

from .models import UserLibrary


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLibrary
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLibrary
        fields = ("email", "password", "first_name")


class MemberSerializer:
    class Meta:
        fields = "email,first_name"
