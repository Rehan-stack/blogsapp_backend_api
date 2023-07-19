from django.urls import path
from .views import *

urlpatterns = [
    path('list',blog_list.as_view()),
    path('details/<int:pk>',Blogs_details.as_view()),
    path('comment/<int:pk>',create_comment.as_view()),
    path('comment_detail/<int:pk>',detail_comment.as_view()),
 
]
