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

@receiver(post_save, sender=Product)
def product_create_signal(sender, instance, created, **kwargs):
    if created:
        from apps.products.use_cases import create_single_product_to_channel
        # TODO: ADD CELERY
        create_single_product_to_channel(instance)


class Channel(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self):
        return self.name

@receiver(post_save, sender=Channel)
def product_change_create_signal(sender, instance, created, **kwargs):
    from apps.products.use_cases import create_bulk_product_to_channel_use_case
    if created:
        # TODO: ADD CELERY
        create_bulk_product_to_channel_use_case(instance)


class ProductChannel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="product_channels")
    channel = models.ForeignKey(Channel, on_delete=models.PROTECT, related_name="product_channels")
    price = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        verbose_name = 'ProductChannel'
        verbose_name_plural = 'Product Channels'
        unique_together = ('product', 'channel')

    def __str__(self):
        return f"product: {self.product.name} - channel: {self.channel.name}"