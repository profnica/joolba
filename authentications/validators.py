from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model


User = get_user_model()
    
def email_validator(value):

    try:
        validate_email(value)
    except ValidationError:
        raise ValidationError(_("Please enter a valid email address"))

