from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class ResgisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',  'password')
        extra_kwargs = {'password': {'write_only': True}}

    def insert_token(self, user):
        token = Token.objects.create(user=user)

        return token.key