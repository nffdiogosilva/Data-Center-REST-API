from django.urls import include, path

from .views import best_datacenter_setup


urlpatterns = [
    path('best-dc-setup', best_datacenter_setup),
]
