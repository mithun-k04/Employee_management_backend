from rest_framework import serializers
from .models import *

class HradminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hradmin
        fields = ['email','password']
        
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveModel
        fields = '__all__'