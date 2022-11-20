from django.urls import include, path

from . import views

# URL Config
urlpatterns = [
    path('hello/', views.say_hello),
    path('register/', views.register_request),
    path('login/', views.login_request)
]
