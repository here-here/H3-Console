from django.conf.urls import include, url
import django
from django.contrib import admin
# from class_periods import views
from .views import RequestTokenView, ValidateTokenView, InvalidateTokenView, ClassesView, CheckInView
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
  url(r'requestToken', RequestTokenView.as_view()),
  url(r'invalidateToken', InvalidateTokenView.as_view()),
  url(r'validateToken', ValidateTokenView.as_view()),

  # Classroom Management for Professors 
  url(r'classes', ClassesView.as_view()),
  url(r'checkins', CheckInView.as_view())
]
