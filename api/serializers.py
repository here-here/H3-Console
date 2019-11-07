from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import Institutions, Students, Sessions, Courses, AttendanceRecord
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id","username","email","date_joined")

class InstitutionsSerializer(ModelSerializer):

    class Meta:
        model = Institutions
        fields = '__all__'


class StudentsSerializer(ModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Students
        fields = "__all__"


# class SchedulesSerializer(ModelSerializer):

#     class Meta:
#         model = Schedules
#         fields = '__all__'


class CoursesSerializer(ModelSerializer):
    # start_time = serializers.SerializerMethodField(source='start_time')
    # end_time = serializers.SerializerMethodField(source='end_time')

    class Meta:
        model = Courses
        fields = '__all__'


class SessionsSerializer(ModelSerializer):

    class Meta:
        model = Sessions
        fields = '__all__'


class AttendanceRecordSerializer(ModelSerializer):

    class Meta:
        model = AttendanceRecord
        fields = '__all__'
