import pytest

from rest_framework.test import APIClient

@pytest.fixture(autouse=True)
@pytest.mark.django_db
def mark_django_db():
    yield


@pytest.fixture
def api_client():
   return APIClient()
