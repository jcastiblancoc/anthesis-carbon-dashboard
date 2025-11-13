import pytest
from api.models import Emission


@pytest.mark.unit
class TestEmissionModel:
    """Test cases for Emission model"""

    def test_create_emission(self):
        """Test creating an emission record with all required fields"""
        emission = Emission.objects.create(
            year=2023,
            emissions=5.5,
            emission_type="CO2",
            country="United Kingdom",
            activity="Air travel"
        )
        
        assert emission.id is not None
        assert emission.year == 2023
        assert emission.emissions == 5.5
        assert emission.emission_type == "CO2"
        assert emission.country == "United Kingdom"
        assert emission.activity == "Air travel"

    def test_emission_str_representation(self):
        """Test string representation of emission"""
        emission = Emission.objects.create(
            year=2023,
            emissions=5.5,
            emission_type="CO2",
            country="United Kingdom",
            activity="Air travel"
        )
        
        expected = "United Kingdom - Air travel (2023): 5.5 CO2"
        assert str(emission) == expected
