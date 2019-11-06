from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from classes.serializers import InstitutionsSerializer, StudentsSerializer, CoursesSerializer, SessionsSerializer, AttendanceRecordSerializer
from classes.models import Institutions, Students, Courses, Sessions, AttendanceRecord


class InstitutionsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Institutions.objects.get(pk=id)
            serializer = InstitutionsSerializer(item)
            return Response(serializer.data)
        except Institutions.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Institutions.objects.get(pk=id)
        except Institutions.DoesNotExist:
            return Response(status=404)
        serializer = InstitutionsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Institutions.objects.get(pk=id)
        except Institutions.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class InstitutionsAPIListView(APIView):

    def get(self, request, format=None):
        items = Institutions.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = InstitutionsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = InstitutionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class StudentsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Students.objects.get(pk=id)
            serializer = StudentsSerializer(item)
            return Response(serializer.data)
        except Students.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Students.objects.get(pk=id)
        except Students.DoesNotExist:
            return Response(status=404)
        serializer = StudentsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Students.objects.get(pk=id)
        except Students.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class StudentsAPIListView(APIView):

    def get(self, request, format=None):
        items = Students.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = StudentsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CoursesAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Courses.objects.get(pk=id)
            serializer = CoursesSerializer(item)
            return Response(serializer.data)
        except Courses.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Courses.objects.get(pk=id)
        except Courses.DoesNotExist:
            return Response(status=404)
        serializer = CoursesSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Courses.objects.get(pk=id)
        except Courses.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CoursesAPIListView(APIView):

    def get(self, request, format=None):
        items = Courses.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = CoursesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SessionsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Sessions.objects.get(pk=id)
            serializer = SessionsSerializer(item)
            return Response(serializer.data)
        except Sessions.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Sessions.objects.get(pk=id)
        except Sessions.DoesNotExist:
            return Response(status=404)
        serializer = SessionsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Sessions.objects.get(pk=id)
        except Sessions.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SessionsAPIListView(APIView):

    def get(self, request, format=None):
        items = Sessions.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SessionsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SessionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AttendanceRecordAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AttendanceRecord.objects.get(pk=id)
            serializer = AttendanceRecordSerializer(item)
            return Response(serializer.data)
        except AttendanceRecord.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AttendanceRecord.objects.get(pk=id)
        except AttendanceRecord.DoesNotExist:
            return Response(status=404)
        serializer = AttendanceRecordSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AttendanceRecord.objects.get(pk=id)
        except AttendanceRecord.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AttendanceRecordAPIListView(APIView):

    def get(self, request, format=None):
        items = AttendanceRecord.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AttendanceRecordSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AttendanceRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
