# This is where our API of our app is stored
from django.urls import path, include  # Used to include lists of URLs

from rest_framework.routers import DefaultRouter

from profiles_api import views

# Create a router and register our ViewSet with it
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet) # the reason I didn't include basename here is because i included query set in views.py
router.register('feed', views.UserProfilesFeedViewSet)


# URL patterns for our API views
urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),  # For APIView
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)) # For ViewSet using router
]
