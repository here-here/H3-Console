from django.conf.urls import include, url
import django
from django.contrib import admin
from class_periods import views
from rest_framework_swagger.views import get_swagger_view

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_swagger_view(title='H3 API')

urlpatterns = [

  # Swagger
  url(r'^docs', schema_view),

  # Session Management
  url(r'requestToken', views.RequestTokenView.as_view()),
  url(r'validateToken', views.ValidateTokenView.as_view()),
  url(r'invalidateToken', views.InvalidateTokenView.as_view()),

  # Classroom Management for Professors 
  url(r'classes', views.ClassesView.as_view()),
  url(r'checkins', views.CheckInView.as_view())
]
