# This is where our API of our app is stored
from django.urls import path
from profiles_api import views
# This is how to call the class to be rendered by our URLS
urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
]
