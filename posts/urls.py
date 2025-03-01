from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="feed"),
    path('<slug:slug>', views.post, name="post" )
]