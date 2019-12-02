from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from django.utils.timezone import now
import uuid

#class User(AbstractUser):
#    is_professor = models.BooleanField(default=False)

class ClassPeriods(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=60)
    location = models.TextField(max_length=150)
    description = models.TextField(max_length=150)
    prefix = models.TextField(max_length=4)
    code = models.TextField(max_length=6)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Class Periods"

class SessionTokens(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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

    class Meta:
        verbose_name_plural="Session Tokens"

class StudentCheckin(models.Model):
    name = models.TextField()
    pid = models.TextField()
    hwid = models.TextField(default="")
    checkin_date = models.DateTimeField(default=timezone.now)
    session = models.ForeignKey(SessionTokens, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} checked in to {self.session.class_period.name} at {self.checkin_date}"

    def save(self, *args, **kwargs): 
        if not self.id:
            self.created = timezone.now()
            self.modified = timezone.now()
            return super(StudentCheckin, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural="Checkins"