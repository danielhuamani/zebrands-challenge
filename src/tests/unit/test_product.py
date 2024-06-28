from rest_framework import status
from apps.products.models import Product


def test_product_error_invalid_permission(api_client, user_superadmin, user_simple, invalid_permission):
    api_client.force_authenticate(user=user_simple)
    response = api_client.post('/api/products/')
    assert response.json()['detail'] == invalid_permission


def test_product_api_list(api_client, user_superadmin, user_simple, product_mappa, product_brugmann):
    api_client.force_authenticate(user=user_simple)
    response = api_client.get('/api/products/')
    assert response.json()["pages"]["count"] == 2

def test_product_api_create_invalid_permission(api_client, user_superadmin, user_simple, invalid_permission):
    api_client.force_authenticate(user=user_simple)
    response = api_client.post('/api/products/')
    assert response.json()['detail'] == invalid_permission

def test_product_api_update_invalid_permission(api_client, user_superadmin, user_simple, product_mappa, invalid_permission):
    api_client.force_authenticate(user=user_simple)
    response = api_client.put(f'/api/products/{product_mappa.id}/')
    assert response.json()['detail'] == invalid_permission

def test_product_api_create(api_client, user_superadmin, user_simple, brand_mappa):
    api_client.force_authenticate(user=user_superadmin)
    response = api_client.post('/api/products/', data={
        "brand": brand_mappa.id,
        "name": "Bolsa de Viaje Weekender Mappa Marron",
        "price": 1.679,
        "sku": "MALETA1",
        "stock": 1000,
        "quantity": 20
    })
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["brand"] == brand_mappa.id
    assert response.json()["name"] == "Bolsa de Viaje Weekender Mappa Marron"
    assert response.json()["sku"] == "MALETA1"

def test_product_api_detail_visit(api_client, user_superadmin, user_simple, product_mappa):
    response = api_client.get(f'/api/products/{product_mappa.id}/')
    p = Product.objects.get(id=product_mappa.id)
    assert response.status_code == status.HTTP_200_OK
    assert p.visits == 1

