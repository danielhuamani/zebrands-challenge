from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.accounts.models import User
from apps.accounts.serializers import UserRegisterSerializer, UserSerializer, UserChangePasswordSerializer
from apps.core.pagination import CorePagination
from apps.core.permissions import AuthenticatedJWT


class UserViewSet(AuthenticatedJWT, ModelViewSet):
    queryset = User.remove_objects.all()
    serializer_class = UserSerializer
    pagination_class = CorePagination

    @swagger_auto_schema(
        request_body=UserRegisterSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                description="User Create",
                schema=UserSerializer,
            )
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        headers = self.get_success_headers(serializer.data)
        serializer_response = UserSerializer(instance)
        return Response(serializer_response.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(
        request_body=UserChangePasswordSerializer,
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="User Create",
                examples={
                    "application/json": {"status": "password set"}
                }
            )
        }
    )
    @action(detail=True, methods=['put'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = UserChangePasswordSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        if not user.check_password(serializer.validated_data['old_password']):
            return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"status": "password set"}, status=status.HTTP_200_OK)
