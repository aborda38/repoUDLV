from rest_framework import routers

from .viewsets import LibrosViewSet

router = routers.SimpleRouter()
router.register('', LibrosViewSet)

urlpatterns = router.urls