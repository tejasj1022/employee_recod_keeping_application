from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("employees.urls")),
    path("api/token/", ObtainAuthToken.as_view()),
]
