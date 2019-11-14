"""h3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# from h3.views import APIRootView, HomeView
# from users.views import LoginView, LogoutView

# from .admin import admin_site

# import home.views
from .views import LoginView, LogoutView, SignupView
from rest_framework import routers
from api import urls as api_urls
from console import urls as console_urls
from django.contrib import admin

# router = routers.DefaultRouter()
# router.register(r'institutions', views.InstitutionsViewSet)
# from classes.u

urlpatterns = [
    path('', include('console.urls')),
    

    # Base
    # path(r'', HomeView.as_view(), name='home')

    # Users
    path(r'login/', LoginView.as_view(), name='login'),
    path(r'logout/', LogoutView.as_view(), name='logout'),
    path(r'signup/', SignupView.as_view(), name='signup'),

    # API
    path(r'^api/', include(api_urls.urlpatterns)),
    # path(r'api/', APIRootView.as_view(), name='api-root')
    # re_path(r'^api/swagger(?P<format>.json|.yaml)$', schema_view.without_ui(), name='schema_swagger'),

    # Admin Page
    path(r'admin/', admin.site.urls)

]
