from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

# from load 

urlpatterns = [
    path('load-impact/', include('loadimpact.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
