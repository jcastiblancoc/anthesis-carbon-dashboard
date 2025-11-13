from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Emission
from .serializers import EmissionSerializer
from .filters import EmissionFilter

class EmissionViewSet(viewsets.ModelViewSet):
    queryset = Emission.objects.all().order_by('id')
    serializer_class = EmissionSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = EmissionFilter
    ordering_fields = ['id', 'year', 'emissions', 'country', 'emission_type', 'activity']
    ordering = ['id']
