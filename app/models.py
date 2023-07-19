from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    acttive= models.BooleanField(default=True)


    def __str__(self):
        return self.title
    

class Comments(models.Model):
    blogs = models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name='blogs')
    comment_user = models.ForeignKey(User,on_delete=models.CASCADE)

    comment = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.comment_user)