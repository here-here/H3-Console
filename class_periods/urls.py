from django.conf.urls import include, url
import django
from django.contrib import admin
from class_periods import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt import views as jwt_views

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_swagger_view(title='H3 API')

urlpatterns = [

  # Swagger
  url(r'^docs', schema_view),

  # JWT Token Endpoints
  url(r'token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  url(r'token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
  # Session Management
  url(r'requestToken', views.RequestTokenView.as_view()),
  url(r'validateToken', views.ValidateTokenView.as_view()),
  url(r'invalidateToken', views.InvalidateTokenView.as_view()),

  # Classroom Management for Professors 
  url(r'classes', views.ClassesView.as_view()),
  url(r'checkins', views.CheckInView.as_view())
]
