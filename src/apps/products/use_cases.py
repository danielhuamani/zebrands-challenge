from apps.products.models import Product, ProductChannel, Channel

def product_add_visit(product):
    product.visits = product.visits + 1
    product.save()

def create_bulk_product_to_channel_use_case(channel):
    product_channel_bulk_create = []
    for product in Product.objects.all():
        product_channel_bulk_create.append(ProductChannel(product=product, channel=channel, price=product.price))
    ProductChannel.objects.bulk_create(product_channel_bulk_create)


def create_single_product_to_channel(product):
    product_channel_bulk_create = []
    for channel in Channel.objects.all():
        product_channel_bulk_create.append(ProductChannel(product=product, channel=channel, price=product.price))
    ProductChannel.objects.bulk_create(product_channel_bulk_create)