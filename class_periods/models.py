from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone

#class User(AbstractUser):
#    is_professor = models.BooleanField(default=False)

class ClassPeriods(models.Model):
    name = models.TextField(max_length=60)
    location = models.TextField(max_length=150)
    description = models.TextField(max_length=150)
    prefix = models.TextField(max_length=4)
    code = models.TextField(max_length=6)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SessionTokens(models.Model):
    token = models.TextField()
    class_period = models.ForeignKey(ClassPeriods, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField(blank=True, null=True)

    def isValid(self):
        if self.expiration_date:
            return self.expiration_date > timezone.now()
        else:
            return True

    def expire(self):
        self.expiration_date = timezone.now()
    
    def __str__(self):
        return self.token

class StudentCheckin(models.Model):
    name = models.TextField()
    pid = models.TextField()
    checkin_date = models.DateTimeField(auto_now=True)
    session = models.ForeignKey(SessionTokens, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} checked in to {self.session.class_period.name} at {self.checkin_date}"
