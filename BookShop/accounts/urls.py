from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register', register_page, name='register'),
    path('login', login_page, name='login'),
    path('logout', logout_request, name='logout'),
    path('user_page', user_page, name='user_page'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate')
]
