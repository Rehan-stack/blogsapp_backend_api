from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError



class Authentication_serializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')

        if password !=password2:
            raise ValidationError('both paswords not match')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)