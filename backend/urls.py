from django.urls import path, include
from  django.contrib import admin
from rest_framework.routers import DefaultRouter
from beotura import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'places', views.PlaceViewSet)
router.register(r'tours', views.TourViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]