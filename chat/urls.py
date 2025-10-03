from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.user_list, name="user_list"),
    path("chat/<str:username>/", views.private_chat, name="private_chat"),
]
