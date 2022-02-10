from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ImageViewSet


urlpatterns = [
    path('image/', ImageViewSet.create),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
