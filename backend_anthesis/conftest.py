import pytest
from rest_framework.test import APIClient
from api.models import Emission


@pytest.fixture
def api_client():
    """Fixture for DRF API client"""
    return APIClient()


@pytest.fixture
def sample_emission():
    """Fixture for a single emission record"""
    return Emission.objects.create(
        year=2023,
        emissions=5.5,
        emission_type="CO2",
        country="United Kingdom",
        activity="Air travel"
    )


@pytest.fixture
def multiple_emissions():
    """Fixture for multiple emission records"""
    emissions = [
        Emission(year=2020, emissions=3.2, emission_type="CO2", country="United States", activity="Manufacturing"),
        Emission(year=2021, emissions=4.5, emission_type="N2O", country="Germany", activity="Agriculture"),
        Emission(year=2022, emissions=6.8, emission_type="CH4", country="France", activity="Waste"),
        Emission(year=2023, emissions=2.1, emission_type="SF6", country="Spain", activity="Energy production"),
        Emission(year=2024, emissions=7.9, emission_type="CO2", country="Italy", activity="Transportation"),
    ]
    return Emission.objects.bulk_create(emissions)


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Enable database access for all tests"""
    pass
