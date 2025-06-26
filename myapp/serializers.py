from rest_framework import serializers
from .models import *

class HradminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hradmin
        fields = ['email','password']
        
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
<<<<<<< HEAD
        fields = '__all__'


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveModel
=======
>>>>>>> 62506c085f34622a671ae78a64637786ee561545
        fields = '__all__'