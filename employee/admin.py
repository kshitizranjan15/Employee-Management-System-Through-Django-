from django.contrib import admin
from .models import Employee, Department,Project,Feedback,LeaveRequest, askHR
# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Feedback)
admin.site.register(LeaveRequest)
admin.site.register(askHR)

