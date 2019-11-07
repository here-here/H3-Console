from django.conf.urls import include, url
import django
from django.contrib import admin
from api import views


urlpatterns = [

  url(r'^institutions/(?P<id>[0-9]+)$', views.InstitutionsAPIView.as_view()),
  url(r'^institutions/$', views.InstitutionsAPIListView.as_view()),

  url(r'^students/(?P<id>[0-9]+)$', views.StudentsAPIView.as_view()),
  url(r'^students/$', views.StudentsAPIListView.as_view()),

  url(r'^courses/(?P<id>[0-9]+)$', views.CoursesAPIView.as_view()),
  url(r'^courses/$', views.CoursesAPIListView.as_view()),

  url(r'^sessions/(?P<id>[0-9]+)$', views.SessionsAPIView.as_view()),
  url(r'^sessions/$', views.SessionsAPIListView.as_view()),

  url(r'^attendancerecord/(?P<id>[0-9]+)$', views.AttendanceRecordAPIView.as_view()),
  url(r'^attendancerecord/$', views.AttendanceRecordAPIListView.as_view()),

]
