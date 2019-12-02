# from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import SessionTokens, ClassPeriods, StudentCheckin
import json
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
# from api.serializers import InstitutionsSerializer, StudentsSerializer, CoursesSerializer, SessionsSerializer, AttendanceRecordSerializer
# from api.models import Institutions, Students, Courses, Sessions, AttendanceRecord


class RequestTokenView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        """Submit a token to create a session"""
        try:
            class_name = request.data['class_name']
            token = request.data['token']
        except:
            return Response(data={'error': 'invalid request'}, status=400)

        if not ClassPeriods.objects.filter(name=class_name).exists():
            return Response(data={'error': 'class does not exist'}, status=400)

        class_section = ClassPeriods.objects.get(name=class_name)
        if SessionTokens.objects.filter(token=token).exists():
            return Response(data={'error': 'existing token'}, status=400)
        token = SessionTokens(token=token, class_period=class_section)
        token.save()

        all_tokens = SessionTokens.objects.all()
        all_tokens_strings = [str(x) for x in all_tokens]
        return Response(data={'status': all_tokens_strings, 'length': len(all_tokens)}, status=200)

class ValidateTokenView(APIView):
    def get(self, request):
        """Admins can see all valid tokens"""
        tokens = SessionTokens.objects.all().values()
        return Response(data={'tokens': tokens})

    def post(self, request):
        """Student wants to validate a token with the server
        
        {
            'token': '6a204bd89f3c8348afd5c77c717a097a',
            'name': 'Peyton Duncan',
            'pid': '1234567',
            'hwid': 'asdfasdf',
        }
        """
        try:
            student_name = request.data['name']
            token = request.data['token']
            pid = request.data['pid']
            hwid = request.data['hwid']
        except:
            return Response(data={'error':'invalid input'}, status=400)

        logger.info(f"Student {student_name} is attempting to validate token {token}")
        
        try:
            matching_token = SessionTokens.objects.get(token=token)
        except:
            return Response(data={'error':'invalid token'}, status=400)
        
        if matching_token.isValid():
            all_objs = StudentCheckin.objects.all()
            conflicts = all_objs.filter(pid=pid) | all_objs.filter(hwid=hwid) | all_objs.filter(name=student_name)
            if conflicts.exists():
                return Response(data={'error': 'Already Checked In'}, status=400)
            checkin = StudentCheckin(name=student_name, pid=pid, session = matching_token)
            checkin.save()
            return Response(status=200)
        else:
            return Response(data={'error':'expired token'}, status=400)


class InvalidateTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Invalidate a class token

        TODO: Only professors and admins should be able to do this
        """
        # return Response("hi")
        try:
            token = request.data['token']
        except:
            return Response(data={'error': 'invalid input'}, status=400)
        
        logger.info(f"Invalidating token {token}")

        try:
            matching_token = SessionTokens.objects.get(token=token)
        except:
            return Response(data={'error':'invalid token'}, status=400)
        
        if matching_token.isValid():
            matching_token.expire()
            matching_token.save()
        
        return Response(status=200)

class CheckInView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        """View all classroom checkins

        TODO: Only professors and admins should be able to view this.
        """
        checkins = StudentCheckin.objects.all()
        string_checkins = [str(x) for x in checkins]
        return Response(data={'checkins': string_checkins})

class ClassesView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        """Retrieve all of a user's classes"""
        classes = ClassPeriods.objects.all().filter(owner=request.user)
        class_strings = [str(x) for x in classes]

        return Response(data={'classes': class_strings})
