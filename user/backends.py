from django.contrib.auth.backends import ModelBackend
from .models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, email, password=None, username=None, **kwargs):
        try:
            user = User.objects.get(email= email)
        except User.DoesNotExist:
            pass