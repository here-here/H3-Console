from django.db import models
from django.contrib.auth.models import User

class Institutions(models.Model):
    name = models.TextField()

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Courses(models.Model):
    name = models.TextField()
    description = models.TextField()
    datepattern = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    students = models.ManyToManyField(Students, blank=True, null=True)
    teachers = models.ManyToManyField(User, blank=True, null=True)

class Sessions(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

class AttendanceRecord(models.Model):
    timestamp = models.DateTimeField()
    mesage = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    session = models.ForeignKey(Sessions, on_delete=models.CASCADE)

