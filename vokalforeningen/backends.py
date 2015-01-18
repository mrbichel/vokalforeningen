from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class EmailBackend(ModelBackend):
    """
    Authenticates against django.contrib.auth.models.User.
    """
    def authenticate(self, username=None, password=None):
        #If username is an email address, then try to pull it up

        try:
            validate_email(username);
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return None

        except ValidationError:
            #We have a non-email address username we
            #should try username
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        if user.check_password(password):
            return user
