from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.products.serializers import BrandSerializer, ProductSerializer
from apps.products.models import Brand, Product
from apps.core.pagination import CorePagination
from apps.core.permissions import AuthenticatedJWT
from apps.products.use_cases import product_add_visit


class BrandViewSet(AuthenticatedJWT, ModelViewSet):
    queryset = Brand.remove_objects.all()
    serializer_class = BrandSerializer


class ProductViewSet(AuthenticatedJWT, ModelViewSet):
    queryset = Product.remove_objects.all()
    serializer_class = ProductSerializer
    pagination_class = CorePagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if not request.user.is_authenticated:
            product_add_visit(instance)
        return Response(serializer.data)

    def get_permissions(self):
        permission_classes = []
        if not self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
