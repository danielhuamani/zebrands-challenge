import pytest
from apps.products.models import Brand, Product

@pytest.fixture
def brand_brugmann(db):
    return Brand.objects.create(name="brugmann")

@pytest.fixture
def brand_mappa(db):
    return Brand.objects.create(name="mappa")


@pytest.fixture
def product_mappa(db, brand_mappa):
    return Product.objects.create(
        brand=brand_mappa, name="Bolsa de Viaje Weekender Mappa Negra",
        price=1.679, sku="MALETA", stock=1000, quantity=20)


@pytest.fixture
def product_brugmann(db, brand_brugmann):
    return Product.objects.create(
        brand=brand_brugmann, name="Cafetera",
        price=700.40, sku="CAFETERA", stock=1000, quantity=10)