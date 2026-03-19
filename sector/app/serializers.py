from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class SectorSerializer(serializers.Serializer):
    sector = serializers.CharField()

    def validate_sector(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Only letters allowed")
        return value.lower()
    
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    confirmpassword=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["email","password","confirmpassword"]
    
    def validate(self,data):
        password=data["password"]
        confirmpassword=data["confirmpassword"]
        if password!=confirmpassword:
            raise serializers.ValidationError("Passwords do not match")
        return data
    def create(self,validated_data):
        user=User.objects.create_user(email=validated_data["email"],password=validated_data["password"])
        return user

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs.get("refresh")
        try:
            RefreshToken(self.token)
        except TokenError:
            raise ValidationError("Invalid or expired refresh token")
        return attrs
    def save(self):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            raise ValidationError("Token already blacklisted or invalid")