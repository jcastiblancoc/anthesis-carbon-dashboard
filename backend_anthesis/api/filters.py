import django_filters
from .models import Emission

class EmissionFilter(django_filters.FilterSet):
    class Meta:
        model = Emission
        fields = {
            'year': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'emissions': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'emission_type': ['exact', 'icontains'],
            'country': ['exact', 'icontains'],
            'activity': ['exact', 'icontains'],
        }
