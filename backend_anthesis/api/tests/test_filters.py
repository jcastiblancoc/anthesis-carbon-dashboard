import pytest
from api.models import Emission
from api.filters import EmissionFilter


@pytest.mark.unit
class TestEmissionFilter:
    """Test cases for EmissionFilter"""

    def test_filter_by_country(self, multiple_emissions):
        """Test filtering emissions by country"""
        filterset = EmissionFilter(
            data={'country': 'Germany'},
            queryset=Emission.objects.all()
        )
        
        assert filterset.is_valid()
        assert filterset.qs.count() == 1
        assert filterset.qs.first().country == 'Germany'

    def test_filter_by_year(self, multiple_emissions):
        """Test filtering emissions by year"""
        filterset = EmissionFilter(
            data={'year': 2023},
            queryset=Emission.objects.all()
        )
        
        assert filterset.is_valid()
        assert filterset.qs.count() == 1
        assert filterset.qs.first().year == 2023
