from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.core.models import (CoreActiveModel, CoreSeoSlugModel,
                              CorePositionModel, CoreRemovedModel, CoreTimeModel)


class Brand(CoreTimeModel, CoreRemovedModel):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
    
    def __str__(self) -> str:
        return self.name


class Product(CoreActiveModel, CoreRemovedModel, CoreSeoSlugModel, CorePositionModel, CoreTimeModel):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True)
    stock = models.PositiveIntegerField()
    visits = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self) -> str:
        return self.name


@receiver(post_save, sender=Product)
def product_update_signal(sender, instance, created, **kwargs):
    if not created:
        # TODO: ADD SEND EMAIL
        ...
