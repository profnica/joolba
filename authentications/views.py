from django.db import IntegrityError
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer, MyTokenObtainPairSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, views
from rest_framework.response import Response
from .utils import send_verification_mail, create_token_for_user
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny


User = get_user_model()


class AccountVerification(views.APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({'message': 'Account verified!'})

# create new user
class UserRegister(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # create tokens for each users that will be returned as a response
        # token = create_token_for_user(user)

        # get the domain name of the site
        current_site = request.get_host()
            
        # send mail
        send_verification_mail(current_site, user)

        return Response({
            # 'token':token.key, 
            'user': UserSerializer(user, context={'request': request}).data,
            'message':'Sign up successful! A verification mail has been sent to your email, please click on the mail'
            }, status=status.HTTP_201_CREATED)
    
    
    

# using jwt to handle token when user log in
class UserLogin(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = [AllowAny]