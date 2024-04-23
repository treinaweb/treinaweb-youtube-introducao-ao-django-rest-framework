from rest_framework import routers

from .views import SkillViewSet


app_name = "skills"
router = routers.SimpleRouter()
router.register(r"", SkillViewSet, basename="skill")
urlpatterns = router.urls
