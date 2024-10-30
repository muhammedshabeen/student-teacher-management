from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import TeacherStudent

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'user_type']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            user_type=validated_data['user_type']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class TeacherStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherStudent
        fields = ['teacher', 'student']
