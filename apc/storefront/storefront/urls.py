"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from shoppingcart.home.views import Index, About, Menu, Contact, Gallery, all_menu, Login, Signup
=======
from shoppingcart.home.views import Index, About, Menu, Contact, Gallery
>>>>>>> 62d58ddb4d6e8b52a7d484198141a80062872014



urlpatterns = [
    path('admin/', admin.site.urls),
    path('shoppingcart/', include('shoppingcart.home.urls')),
    path('_debug_/', include(debug_toolbar.urls)),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
<<<<<<< HEAD
    path('menu/', all_menu, name='menu'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
=======
    path('menu/', Menu.as_view(), name='menu'),
>>>>>>> 62d58ddb4d6e8b52a7d484198141a80062872014
    path('contact/', Contact.as_view(), name='contact'),
    path('gallery/', Gallery.as_view(), name='gallery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  

