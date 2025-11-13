from rest_framework.routers import DefaultRouter
from .views import EmissionViewSet

router = DefaultRouter()
router.register(r'emissions', EmissionViewSet, basename='emission')

urlpatterns = router.urls
