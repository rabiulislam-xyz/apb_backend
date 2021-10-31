from django.contrib.auth import get_user_model
from rest_framework import viewsets
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from apb_backend.settings import env
from .serializers import UserSerializer

User = get_user_model()

CALLBACK_URL = env.str('CALLBACK_URL', 'http://localhost:3000/login')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GoogleLogin(SocialLoginView):
    authentication_classes = []  # disable authentication
    adapter_class = GoogleOAuth2Adapter
    callback_url = CALLBACK_URL
    client_class = OAuth2Client
