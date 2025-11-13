import os
import django
import random
from config.logger import setup_logger

# Setup logger
logger = setup_logger(__name__)

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from api.models import Emission

def seed_data():
    """Seed the database with mock emission data"""
    
    # Clear existing data
    Emission.objects.all().delete()
    logger.info("Cleared existing emission data")
    
    # Mock data
    emission_types = ['CO2', 'N2O', 'CH4', 'SF6']
    countries = ['United Kingdom', 'United States', 'Germany', 'France', 'Spain', 'Italy', 'Canada', 'Japan']
    activities = ['Air travel', 'Waste', 'Manufacturing', 'Transportation', 'Energy production', 'Agriculture', 'Residential']
    
    mock_data = [
        {
            "year": 2015,
            "emissions": 5.2,
            "emission_type": "CO2",
            "country": "United Kingdom",
            "activity": "Air travel",
        },
        {
            "year": 2016,
            "emissions": 2.9,
            "emission_type": "N2O",
            "country": "United Kingdom",
            "activity": "Waste",
        },
        {
            "year": 2017,
            "emissions": 8.5,
            "emission_type": "CO2",
            "country": "United States",
            "activity": "Manufacturing",
        },
        {
            "year": 2018,
            "emissions": 4.3,
            "emission_type": "CH4",
            "country": "Germany",
            "activity": "Agriculture",
        },
        {
            "year": 2019,
            "emissions": 6.7,
            "emission_type": "CO2",
            "country": "France",
            "activity": "Transportation",
        },
        {
            "year": 2020,
            "emissions": 3.1,
            "emission_type": "N2O",
            "country": "Spain",
            "activity": "Energy production",
        },
        {
            "year": 2021,
            "emissions": 7.8,
            "emission_type": "CO2",
            "country": "Italy",
            "activity": "Air travel",
        },
        {
            "year": 2022,
            "emissions": 5.6,
            "emission_type": "SF6",
            "country": "Canada",
            "activity": "Manufacturing",
        },
        {
            "year": 2023,
            "emissions": 4.9,
            "emission_type": "CH4",
            "country": "Japan",
            "activity": "Waste",
        },
        {
            "year": 2024,
            "emissions": 9.2,
            "emission_type": "CO2",
            "country": "United Kingdom",
            "activity": "Energy production",
        },
    ]
    
    # Generate additional random data
    for year in range(2015, 2025):
        for _ in range(5):
            mock_data.append({
                "year": year,
                "emissions": round(random.uniform(1.0, 10.0), 2),
                "emission_type": random.choice(emission_types),
                "country": random.choice(countries),
                "activity": random.choice(activities),
            })
    
    # Create emission objects
    emissions = [
        Emission(
            year=data['year'],
            emissions=data['emissions'],
            emission_type=data['emission_type'],
            country=data['country'],
            activity=data['activity']
        )
        for data in mock_data
    ]
    
    # Bulk create
    Emission.objects.bulk_create(emissions)
    
    logger.info(f"Successfully seeded {len(emissions)} emission records")
    

if __name__ == '__main__':
    seed_data()