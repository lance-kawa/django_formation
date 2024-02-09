"""
URL configuration for pythagore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from faunatrack import views as fauna_views

from rest_framework.routers import DefaultRouter
from faunatrack.api_view import EspeceViewSet, ExampleView
from rest_framework.authtoken import views
# Crée un routeur et enregistre nos viewsets avec lui.
router = DefaultRouter()
router.register(r'especes', EspeceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fauna_views.hello_world, name='home'),
    path('faunatrack/', include('faunatrack.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('example/', ExampleView.as_view(), name="exemple"),
    path('api-token/', views.obtain_auth_token),
    path('api-auth/', include('dj_rest_auth.urls')),
]
