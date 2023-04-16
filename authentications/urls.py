from django.urls import path
from .views import *

urlpatterns = [
    path('user/register', UserRegister.as_view(), name='register-user'),
    path('account/verify/<str:uuidb64>/<str:token>', AccountVerification.as_view(), name='account_verification'),
]
