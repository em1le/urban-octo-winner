from rest_framework.routers import DefaultRouter

from articles.viewsets import ArticleViewSet

router = DefaultRouter()
router.register("", ArticleViewSet, basename="articles")

urlpatterns = router.urls
