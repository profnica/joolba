from django.db import IntegrityError
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, views
from rest_framework.response import Response
from .utils import send_verification_mail

User = get_user_model()


class AccountVerification(views.APIView):
    def get(self, request):
        return Response({'message': 'Account verified!'})

class UserRegister(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # create tokens for each users that will be returned as a response
            try:
                token = Token.objects.create(user=user)
            except IntegrityError:
                token = Token.objects.get(user=user)
                return Response({'error':'token must be unique for each user'}, status=status.HTTP_400_BAD_REQUEST)

            # get the domain name of the site
            current_site = request.get_host()
            
            # send mail
            send_verification_mail(current_site, user)

            return Response({
                'token':token.key,
                'user': serializer.data,
                'message':'sign up successful! A verification mail has been sent to your email, please click on the mail'
                }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    