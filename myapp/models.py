from django.db import models

class Hradmin(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
    
class Employee(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    department = models.CharField(max_length=100, blank=False)
    designation = models.CharField(max_length=100, blank=False)
    join_date = models.DateField()
    
class LeaveModel(models.Model):
<<<<<<< HEAD
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='employee')
=======
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
>>>>>>> 62506c085f34622a671ae78a64637786ee561545
    month = models.CharField(max_length=20)
    sl = models.IntegerField(default=0)  
    cl = models.IntegerField(default=0)  

    def __str__(self):
        return f"{self.employee.name} - {self.month}"
