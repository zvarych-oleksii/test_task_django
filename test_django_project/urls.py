"""URL Configuration for test_django_project project."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('email_validation.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
