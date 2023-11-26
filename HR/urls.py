from . import views
from django.urls import path

urlpatterns = [
    path("", views.dashboard),
    path("profile/", views.edit_profile),
    path("addemployee/", views.add_employee),
    path("deleteemployee/", views.delete_employee),
    path("req/",views.hr_requests_view),
    path("addmanager/", views.assign_manager),
    path("hrfeedbackview/",views.hr_feedback_view),
    path('api/send_employee_email/',views.EmployeeEmailAPI.as_view(), name='send_employee_email'),
]

