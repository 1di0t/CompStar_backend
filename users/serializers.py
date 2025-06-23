from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # create_user는 비밀번호를 자동으로 해싱합니다.
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
