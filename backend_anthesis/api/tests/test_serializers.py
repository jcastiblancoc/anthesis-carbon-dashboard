import pytest
from api.serializers import EmissionSerializer


@pytest.mark.unit
class TestEmissionSerializer:
    """Test cases for EmissionSerializer"""

    def test_serializer_with_valid_data(self):
        """Test serializer creates emission with valid data"""
        data = {
            'year': 2023,
            'emissions': 5.5,
            'emission_type': 'CO2',
            'country': 'United Kingdom',
            'activity': 'Air travel'
        }
        
        serializer = EmissionSerializer(data=data)
        assert serializer.is_valid()
        emission = serializer.save()
        
        assert emission.year == 2023
        assert emission.emissions == 5.5
        assert emission.emission_type == 'CO2'

    def test_serializer_with_invalid_data(self):
        """Test serializer validation with missing required fields"""
        data = {
            'year': 2023,
            'emissions': 5.5
        }
        
        serializer = EmissionSerializer(data=data)
        assert not serializer.is_valid()
        assert 'emission_type' in serializer.errors
        assert 'country' in serializer.errors
        assert 'activity' in serializer.errors
