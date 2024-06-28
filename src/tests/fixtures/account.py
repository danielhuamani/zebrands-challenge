import pytest
from apps.accounts.models import User

@pytest.fixture
def user_superadmin(db):
    u = User.objects.create(email="jhon@example.com", is_superuser=True, is_admin=True)
    u.set_password("password")
    u.save()
    return u

@pytest.fixture
def user_simple(db):
    u = User.objects.create(email="jhon2@example.com", is_admin=False)
    u.set_password("password")
    u.save()
    return u