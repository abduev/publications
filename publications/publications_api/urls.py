from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PublicationsViewSet


v1_router = DefaultRouter()
v1_router.register(r'', PublicationsViewSet, 'publications_api')

urlpatterns = [
    path('', include(v1_router.urls))
]
