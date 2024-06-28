from rest_framework.serializers import ModelSerializer
from apps.products.models import Brand, Product


class BrandSerializer(ModelSerializer):

    class Meta:
        model = Brand
        fields = ["id", "name"]


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "brand", "price", "quantity", "name", "sku", "stock", "visits"]
        read_only_fields = ["visits"]