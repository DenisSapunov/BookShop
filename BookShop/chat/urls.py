from django.urls import path
from .views import *

app_name='chat'

urlpatterns = [
    path('create_not_auth_message', create_not_auth_user_message, name='create_not_auth_user_message'),
    path('just_message', just_message, name='just_message'),
    path('home', home, name='home'),
    path('checkview', checkview, name='checkview'),
    path('send/', send, name='send'),
    path('<str:room>/', room, name='room'),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),
]