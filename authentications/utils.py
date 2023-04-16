from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from joolbabackend.settings import EMAIL_HOST_USER

def send_verification_mail(current_site, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_token = default_token_generator.make_token(user)
    verification_link = reverse('account_verification', kwargs={'uuidb64':uid, 'token':verification_token})
    verification_url = f'http://{current_site}{verification_link}'
    subject = 'Verify your account'
    message = f'Hello {user.name}, \n\nThanks for signing up on Joolba, kindly click on the link below to verify your account \n\n{verification_url}\n\nThank you!\n\nJoolba Team.'
    from_email = EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
