from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/skills/", include("skills.urls", namespace="skills")),
    path("api/jobs/", include("jobs.urls", namespace="jobs")),
]
