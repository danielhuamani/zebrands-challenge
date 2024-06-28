from rest_framework import status
from apps.accounts.models import User

def test_user_error_not_authenticated(api_client, user_superadmin, user_simple, auth_error):
    response = api_client.get('/api/users/')
    assert response.json()['detail'] == auth_error

def test_user_error_not_permission(api_client, user_superadmin, user_simple, invalid_permission):
    api_client.force_authenticate(user=user_simple)
    response = api_client.get('/api/users/')
    assert response.json()['detail'] == invalid_permission

def test_user_api_list(api_client, user_superadmin, user_simple):
    api_client.force_authenticate(user=user_superadmin)
    response = api_client.get('/api/users/')
    assert response.json()["pages"]["count"] == 2
    assert response.status_code == status.HTTP_200_OK

def test_user_api_create(api_client, user_superadmin):
    api_client.force_authenticate(user=user_superadmin)
    response = api_client.post('/api/users/', data={
        "first_name": "jhon",
        "last_name": "doe",
        "email": "john3@example.com",
        "password": "password2",
        "password2": "password2"
    })
    assert response.status_code == status.HTTP_201_CREATED

def test_user_api_detail(api_client, user_superadmin):
    api_client.force_authenticate(user=user_superadmin)
    response = api_client.get(f'/api/users/{user_superadmin.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["email"] == user_superadmin.email
    assert response.json()["first_name"] == user_superadmin.first_name

def test_user_api_update(api_client, user_superadmin):
    api_client.force_authenticate(user=user_superadmin)
    response = api_client.put(f'/api/users/{user_superadmin.id}/', data={
        "email": user_superadmin.email,
        "first_name": "jhon",
        "is_active": user_superadmin.is_active
    })
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["first_name"] == "jhon"


def test_user_api_change_password(api_client, user_superadmin):
    api_client.force_authenticate(user=user_superadmin)
    response = api_client.put(f'/api/users/{user_superadmin.id}/set_password/', data={
        "old_password": "password",
        "new_password": "password2",
    })
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == "password set"

def test_user_api_change_password_invalid(api_client, user_superadmin):
    api_client.force_authenticate(user=user_superadmin)
    response = api_client.put(f'/api/users/{user_superadmin.id}/set_password/', data={
        "old_password": "password3",
        "new_password": "password2",
    })
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_user_api_delete(api_client, user_superadmin, user_simple):
    api_client.force_authenticate(user=user_superadmin)
    response = api_client.delete(f'/api/users/{user_superadmin.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert User.remove_objects.all().count() == 1
    assert User.objects.all().count() == 2

