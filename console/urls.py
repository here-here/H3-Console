from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.IndexView, name="home"),
    path(r'classes', views.ClassesView, name="Classes"),
    path('classes/<uuid:class_id>', views.SessionsView, name="Sessions"),
    path('sessions/<uuid:session_id>', views.AttendanceView, name="Attendance"),
    path('help', views.HelpView, name="help")
]