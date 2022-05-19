from rest_framework.routers import DefaultRouter

from references.viewsets import ReferenceViewSet

router = DefaultRouter()
router.register("", ReferenceViewSet, basename="references")

urlpatterns = router.urls
