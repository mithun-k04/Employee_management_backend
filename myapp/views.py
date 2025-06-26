from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class LoginHrclass(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'message': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Hradmin.objects.get(email=email)
            if password == user.password:
                return Response({'message': 'Hr login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        except Hradmin.DoesNotExist:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        
class AddEmployee(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        department = request.data.get('department')
        designation = request.data.get('designation')
        join_date = request.data.get('join_date')
        
        if not name or not email or not department or not designation or not join_date:
            return Response({'message': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        already = Employee.objects.filter(email=email).exists()
        
        if already:
            return Response({'message': 'Employee already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        newdata = Employee.objects.create(
            name=name,
            email=email,
            department=department,
            designation=designation,
            join_date=join_date
        )
        newdata.save()
        return Response({'message': 'Employee added successfully'}, status=status.HTTP_200_OK)
        