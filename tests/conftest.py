import pytest

from Diplom_2.tests.api_client import APIClient


@pytest.fixture
def api_client():
    return APIClient()