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
from django.contrib.auth import views as auth_views
from django.urls import path, include

# from h3.views import APIRootView, HomeView
# from users.views import LoginView, LogoutView

# from .admin import admin_site

# import home.views
from .views import RedirectView, SignupView
from rest_framework import routers
from class_periods import urls as api_urls
from console import urls as console_urls
from django.contrib import admin

# router = routers.DefaultRouter()
# router.register(r'institutions', views.InstitutionsViewSet)
# from classes.u

urlpatterns = [
    # Redirect home to the console
    path(r'', RedirectView.as_view()),

    # Console URLs
    path(r'console/', include('console.urls')),
    

    # Base
    # path(r'', HomeView.as_view(), name='home')

    # The following line adds the following paths:
    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/signup', SignupView.as_view()),
    path(r'login', auth_views.LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    path(r'logout', auth_views.LogoutView.as_view(), {'next_page': '/login'}, name='logout'),
    # Class Period API
    path(r'api/classes', include(api_urls.urlpatterns)),
    # path(r'api/', APIRootView.as_view(), name='api-root')
    # re_path(r'^api/swagger(?P<format>.json|.yaml)$', schema_view.without_ui(), name='schema_swagger'),

    # Admin Page
    path(r'admin/', admin.site.urls)

]
