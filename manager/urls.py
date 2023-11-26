from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    # path('adddepandpro/',views.assign_dep_project),
    path('', views.dashboard),
    path('mgrrequestsview/',views.mgr_requests_view),
    path('mgrfeedbackview/',views.mgr_feedback_view),
    path('employeeviewstatus/',views.employee_view_status),
    path('assignprodept/',views.assign_pro_dept),
    path('profile/',views.edit_profile),
    path('sendpr/', views.send_pr)
]