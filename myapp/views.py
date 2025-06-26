from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = LeaveModel.objects.all()
    serializer_class = LeaveSerializer


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
        

class GetLeaveById(APIView):
    def get(self, request, id):
        try:
            employee = Employee.objects.get(id=id)
            leaverecords = LeaveModel.objects.filter(employee=employee)
            serializer = LeaveSerializer(leaverecords, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        

class LeaveUpdate(APIView):
    def put(self, request, id):
        print(f"Updated SL and CL for leave ID {id}:")
        leaverecord = LeaveModel.objects.get(id = id)
        leaverecord.sl = request.data.get('sl')
        leaverecord.cl = request.data.get('cl')
        leaverecord.save()
        print("SL:", request.data.get('sl'), "CL:", request.data.get('cl'))
        return Response({"message": "Update received"}, status=status.HTTP_200_OK)


class EmployeeValidation(APIView):
    def post(self, request):
        email = request.data.get('email')
        employee = Employee.objects.get(email = email)
        if employee:
                request.session['empid'] = employee.id
                request.session['empEmail'] = employee.email
                return Response({'message': 'employee login successful'}, status=status.HTTP_200_OK)
        else:
                return Response({'message': 'employee login failed'}, status=status.HTTP_404_NOT_FOUND)

class GetLeaveByEmail(APIView):
    def get(self, request, email):
        try:
            employee = Employee.objects.get(email=email)
            leaverecords = LeaveModel.objects.filter(employee=employee)
            serializer = LeaveSerializer(leaverecords, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)