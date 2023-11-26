import uuid 
from django.db import models 
# Create your models here.

def create_uid():
    return str(uuid.uuid4())

class Employee(models.Model):
    id=models.CharField( 
         max_length=100,
         primary_key = True, 
         default = create_uid(), 
         editable = False) 
    name=models.CharField(max_length=80)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=255)
    designation=models.CharField(max_length=80, default='Employee')
    sick_leave=models.IntegerField(default=12)
    casual_leave=models.IntegerField(default=5)
    annual_leave=models.IntegerField(default=5)
    phone_number=models.IntegerField()
    pid=models.ForeignKey('Project',on_delete=models.CASCADE, null=True, blank=True)
    did=models.ForeignKey('Department',on_delete=models.CASCADE, null=True, blank=True)
    manager_id=models.ForeignKey('Employee',on_delete=models.CASCADE,null=True,blank=True,related_name="manager")
    hr_id=models.ForeignKey('Employee',on_delete=models.CASCADE,null=True,blank=True,related_name="hr")
    status=models.BooleanField(default=False)
    profile_url=models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name_plural='Employee'

class Department(models.Model):
    id=models.CharField( 
         max_length=100,
         primary_key = True, 
         default = str(uuid.uuid4()), 
         editable = False) 
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name_plural='Department'

class Project(models.Model):
    id=models.CharField( 
         max_length=100,
         primary_key = True, 
         default = str(uuid.uuid4()), 
         editable = False) 
    name = models.CharField(max_length=80)
    did=models.ForeignKey('Department',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Project'

class Feedback(models.Model):
    id=models.CharField( 
         max_length=100,
         primary_key = True, 
         default = str(uuid.uuid4()), 
         editable = False) 
    fed_by=models.ForeignKey('Employee',on_delete=models.CASCADE,related_name='given_feedback', null=True, blank=True)
    fed_to=models.ForeignKey('Employee',on_delete=models.CASCADE,related_name='recieved_feedback', null=True, blank=True)
    type=models.CharField(max_length=50)
    fed_body=models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural='Feedback'

class askHR(models.Model):
    id=models.CharField(max_length=100,
        primary_key=True,
        default = str(uuid.uuid4()), 
        editable = False) 
    text=models.TextField()
    hr_id = models.ForeignKey('Employee', on_delete=models.CASCADE, default=None)
    class Meta:
        verbose_name_plural='AskHR'
        
class LeaveRequest(models.Model):
    id = models.CharField( 
         max_length=100,
         primary_key = True, 
        #  default = create_uid(), 
         editable = False)
    date_from = models.DateField(auto_now=False, auto_now_add=False)
    date_to = models.DateField(auto_now=False, auto_now_add=False)
    reason = models.CharField(max_length=100)
    req_to = models.ForeignKey('Employee', on_delete=models.CASCADE, default=None)
    type = models.CharField(max_length=30, default="Casual")

    class Meta:
        verbose_name_plural='LeaveRequest'
