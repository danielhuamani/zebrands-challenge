from django.db import models
from apps.core.models import (CoreActiveModel, CoreSeoSlugModel,
                              CorePositionModel, CoreRemovedModel, CoreTimeModel)


class Brand(CoreRemovedModel, CoreTimeModel):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
    
    def __str__(self) -> str:
        return self.name


class Product(CoreActiveModel, CoreRemovedModel, CoreSeoSlugModel, CorePositionModel, CoreTimeModel):
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True)
    viewers = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self) -> str:
        return self.name