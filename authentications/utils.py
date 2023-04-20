from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from joolbabackend.settings import EMAIL_HOST_USER
from rest_framework.authtoken.models import Token
from django.db import IntegrityError


# this is file contains functions i might need 

# send verification mail

def send_verification_mail(current_site, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_token = default_token_generator.make_token(user)
    verification_link = reverse('account_verification', kwargs={'uuidb64':uid, 'token':verification_token})
    verification_url = f'http://{current_site}{verification_link}'
    subject = 'Confirm your email address for Joolba Account'
    message = f'Dear {user.name}, \n\nThank you for creating an account with Joolba, your go-to source for the latest news and updates. To access our premium content and stay up to date on breaking news, please verify your email address by clicking on the link below: \n\n{verification_url}\n\nIf you did not create an account with Joolba, please ignore this email. Your account will not be actiavted until you verify your email address\n\nThank you for choosing Joolba as your trusted news source. We look forward to keeping you informed on the latest news and event\n\nBest regards,\n\nThe Joolba Team.'
    from_email = EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)


# create token for users on sign up
def create_token_for_user(user):
    try:
        token = Token.objects.create(user=user)
    except IntegrityError:
        token = Token.objects.get(user=user)

    return token