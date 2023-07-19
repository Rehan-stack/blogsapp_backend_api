from django.shortcuts import render
from .serializers import Authentication_serializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from authentication import models
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


@api_view(['POST'])
def delete_user(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)




@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = Authentication_serializer(data=request.data)

        data = {}



        if serializer.is_valid():
            account = serializer.save()

            data['username'] = account.username
            data['email'] = account.email
            data['token'] = Token.objects.get(user=account).key
        else:
            return Response(serializer.errors)
        return Response(data)

