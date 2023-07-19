from django.shortcuts import render
from .serialzers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView
from rest_framework.validators import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
# Create your views here.



class create_comment(CreateAPIView):
    serializer_class = Comments_serializer
    permission_classes = [IsAuthenticated]
    queryset = ''

    def perform_create(self, serializer):

        pk = self.kwargs['pk']
        comment = Blogs.objects.get(id=pk)

        comment_user = self.request.user

        comment_queryset= Comments.objects.filter(comment=comment,comment_user=comment_user)
        if comment_queryset.exists():
            raise ValidationError('you already comment on this blog')
        serializer.save(comment=comment,comment_user=comment_user)
        

class detail_comment(ListAPIView):
    serializer_class = Comments_serializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        comments_user = self.request.user
        return Comments.objects.filter(id=pk,comment_user=comments_user)





class blog_list(ListCreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = Blogs_serializers
    permission_classes = [IsAuthenticated]




class Blogs_details(RetrieveUpdateDestroyAPIView):
    serializer_class = Blogs_serializers
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Blogs.objects.filter(id=pk)
        
