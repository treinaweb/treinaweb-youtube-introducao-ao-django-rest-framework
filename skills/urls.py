from django.urls import path

from .views import SkillListView


app_name = "skills"
urlpatterns = [
    path("", SkillListView.as_view(), name="skill-list"),
]
