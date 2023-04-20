from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', UserLogin.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register', UserRegister.as_view(), name='register_user'),
    path('account/verify/<str:uuidb64>/<str:token>', AccountVerification.as_view(), name='account_verification'),
]

# for the logout the client can simply discard the token and the user will be logged out