from django.urls import path

from .views import SkillListView, SkillDetailView


app_name = "skills"
urlpatterns = [
    path("", SkillListView.as_view(), name="skill-list"),
    path("<int:pk>/", SkillDetailView.as_view(), name="skill-detail"),
]
