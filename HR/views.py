from django.http import HttpResponse,request
from employee.models import Employee,Feedback, askHR, LeaveRequest
from django.shortcuts import render
from HRwhiz.views import session_login_required
import requests
import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
@session_login_required
def dashboard(request):
    return render(request, 'hr.html', {'name': request.session['name'], 'id': request.session['id'], 'designation': request.session['designation'], 'annual_leave': int(request.session['annual_leave']), 'casual_leave': int(request.session['casual_leave']), 'sick_leave': int(request.session['sick_leave'])})

class EmployeeEmailAPI(APIView):
    def post(self, request):
        data = request.data

        subject = "Your Employee Login Information"
        message = f"Hello {data['name']},\n\nYour login email is: {data['email']}\nYour temporary password is: {data['password']}\n\nPlease change your password after initial login."
        from_email = 'hrwhizapp2023@gmail.com'  # Use your own email address
        recipient_list = [data['email']]

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Email sending failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@session_login_required
def add_employee(request):
    response = None
    if request.method == 'POST':
        # Retrieve data from the form
        # id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        designation = request.POST.get('designation')
        sick_leave = request.POST.get('sick_leave')
        casual_leave = request.POST.get('casual_leave')
        annual_leave = request.POST.get('annual_leave')
        phone_number = request.POST.get('phone_number')
        profile_url = request.POST.get('profile_url')

        # Create and save the Employee object
        employee = Employee(
            id=str(uuid.uuid4()),
            name=name,
            email=email,
            password=password,
            address=address,
            designation=designation,
            sick_leave=sick_leave,
            casual_leave=casual_leave,
            annual_leave=annual_leave,
            phone_number=phone_number,
            profile_url=profile_url
        )
        employee.save()
        api_url = 'http://127.0.0.1:8000/HR/addemployee/'  # Adjust the URL as needed
        data = {
            'id': id,
            'name': name,
            'email': email,
            'password': password,
            'subject':'Test sub'
        }
        subject = 'agds'
        message= 'dhsfhj'
        from_email = 'hrwhizapp2023@gmail.com'
        

        response = requests.post(api_url, data=data)

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return HttpResponse({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
        return render(request, 'addemp.html',{'designation':request.session['designation'], 'name': request.session['name']})
    # Log the error for debugging
        # print(f"Email sending error: {str(e)}")
        # return HttpResponse({'error': 'Email sending failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    return render(request, 'addemp.html',{'designation':request.session['designation'], 'name': request.session['name']})

@session_login_required
def success_page(request):
    return HttpResponse("Employee added successfully!")  # You can create a success page here

@session_login_required
def delete_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('id')

        try:
            employee = Employee.objects.get(id=employee_id)
            employee.delete()
            return HttpResponse('Employee removed')  # Redirect to a list view or another page
        except Employee.DoesNotExist:
            error_message = "Employee not found"
    else:
        error_message = None

    return render(request, 'deleteemp.html', {'error_message': error_message,'designation':request.session['designation'], 'name': request.session['name']})

@session_login_required
def hr_requests_view(request):
    # Assuming you have stored the HR's ID in the session as 'hr_id'
    hr_id = request.session.get('id', None)
    
    if hr_id is not None:
        # Filter requests where req_to matches the logged-in HR's ID
        hr_requests = askHR.objects.filter(hr_id=hr_id)
        
        return render(request, 'req.html', {'hr_requests': hr_requests,'designation':request.session['designation'], 'name': request.session['name']})
    else:
        # Handle the case where the HR is not logged in or the session is not set
        # You can redirect to a login page or handle it as per your application's logic.
        return render(request, 'hr.html',)

@session_login_required  
def hr_feedback_view(request):
    # Assuming you have stored the HR's ID in the session as 'hr_id'
    hr_id = request.session.get('id', None)
    
    if hr_id is not None:
        # Filter requests where req_to matches the logged-in HR's ID
        hr_requests = Feedback.objects.filter(fed_to=hr_id)
        
        return render(request, 'reqfeedback.html', {'hr_requests': hr_requests,'designation':request.session['designation'], 'name': request.session['name']})
    else:
        # Handle the case where the HR is not logged in or the session is not set
        # You can redirect to a login page or handle it as per your application's logic.
        return render(request, 'hr.html')

# @session_login_required
# def assign_manager(request):
#     if request.method == 'POST':
#         employee_id = request.POST['employee_id']
#         manager_id = request.POST['manager_id']

#         try:
#             # Retrieve the employee and manager instances
#             employee = Employee.objects.get(id=employee_id)
#             manager = Employee.objects.get(id=manager_id)

#             # Assign the manager to the employee
#             employee.manager_id = manager
#             employee.save()

#             return HttpResponse('Manager Assigned')  
#         except Employee.DoesNotExist:
#             # Handle the case where employee or manager is not found
#             return HttpResponse('Employee or Manager Not Exists')

#     return render(request, 'addmanager.html',{'designation':request.session['designation']})

@session_login_required
def assign_manager(request):
    employees=Employee.objects.filter(designation="Employee")
    emps=Employee.objects.filter(designation="Manager")
    if request.method == 'POST':
        employee_id = request.POST.get("employee_id")
        mgr_id = request.POST.get("manager_id")

        emp_data=Employee.objects.filter(id=employee_id)
        emp_data.update(manager_id=mgr_id)

    return render(request, 'addmanager.html',{"employees":employees,"emps":emps, 'designation':request.session['designation'], 'name': request.session['name']})

@session_login_required
def edit_profile(request):
    data= Employee.objects.filter(id=request.session.get('id', None))
    name=data.first().name
    password=data.first().password
    email=data.first().email
    address=data.first().address
    phone_number=data.first().phone_number

    if request.method=="POST":
        # print("Editing")
        name=request.POST.get("name")
        password=request.POST.get("password")
        email=request.POST.get("email")
        address=request.POST.get("address")
        phone_number=request.POST.get("phone_number")
        data.update(name=name,password=password,email=email,address=address,phone_number=phone_number)
    
    return render(request,"profile.html",{"name":name,"password":password,"email":email,"address":address,"phone_number":phone_number, "designation":request.session['designation'],  'annual_leave': int(request.session['annual_leave']), 'casual_leave': int(request.session['casual_leave']), 'sick_leave': int(request.session['sick_leave'])})