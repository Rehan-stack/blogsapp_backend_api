from .models import *
from rest_framework import serializers




class Comments_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields= '__all__'





class Blogs_serializers(serializers.ModelSerializer):
    blogs = Comments_serializer(many=True,read_only=True)
    class Meta:
        model = Blogs
        fields = '__all__'







  
