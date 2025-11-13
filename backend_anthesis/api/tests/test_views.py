import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.integration
class TestEmissionViewSet:
    """Test cases for EmissionViewSet API endpoints"""

    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        """Setup for each test"""
        self.client = api_client
        self.list_url = reverse('emission-list')

    def test_list_emissions(self, multiple_emissions):
        """Test GET /api/emissions/ returns all emission records"""
        response = self.client.get(self.list_url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 5
        assert all('year' in item for item in response.data)
        assert all('emissions' in item for item in response.data)
        assert all('country' in item for item in response.data)

    def test_filter_by_country(self, multiple_emissions):
        """Test filtering emissions by country parameter"""
        response = self.client.get(self.list_url, {'country': 'Germany'})
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['country'] == 'Germany'
