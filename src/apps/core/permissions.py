from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated


class AuthenticatedJWT:
    authentication_classes = (JWTAuthentication, )
    permission_classes = [IsAuthenticated]
