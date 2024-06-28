from django.urls import path
from rest_framework import routers
from apps.accounts.apis import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = routers.SimpleRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    path('accounts/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
