from django.urls import include, path

from . import views

# URL Config
urlpatterns = [
    path('hello/', views.say_hello)
]
