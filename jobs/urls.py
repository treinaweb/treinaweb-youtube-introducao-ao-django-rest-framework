from rest_framework import routers

from .views import JobViewSet


app_name = "jobs"
router = routers.SimpleRouter()
router.register(r"", JobViewSet, basename="job")
urlpatterns = router.urls
