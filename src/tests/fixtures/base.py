import pytest

@pytest.fixture
def auth_error():
    return 'Authentication credentials were not provided.'

@pytest.fixture
def invalid_permission():
    return 'You do not have permission to perform this action.'