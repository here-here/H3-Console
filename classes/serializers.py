from rest_framework.serializers import ModelSerializer
from classes.models import Institutions, Students, Courses, Sessions, AttendanceRecord


class InstitutionsSerializer(ModelSerializer):

    class Meta:
        model = Institutions
        fields = '__all__'


class StudentsSerializer(ModelSerializer):

    class Meta:
        model = Students
        fields = '__all__'


class CoursesSerializer(ModelSerializer):

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
