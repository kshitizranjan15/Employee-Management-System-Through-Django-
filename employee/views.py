from django.shortcuts import render, redirect
from .models import Feedback, askHR, LeaveRequest, Employee
from django.http import HttpResponse

import uuid
from HRwhiz.views import session_login_required

# Create your views here.\
@session_login_required
def dashboard(request):
    return render(request, 'emp.html', {'name': request.session['name'], 'id': request.session['id'], 'designation': request.session['designation'], 'annual_leave': int(request.session['annual_leave']), 'casual_leave': int(request.session['casual_leave']), 'sick_leave': int(request.session['sick_leave'])})

@session_login_required
def feedback(request):
    if request.method == 'POST':       
        des=request.POST.get('description')
        employee = Employee.objects.filter(id=request.session.get('id', None)).first()
        
        if request.POST.get('selection-value') == 'HR':
            if employee:
                fed_to = employee.hr_id
            else:
                fed_to = None

        elif request.POST.get('selection-value') == 'Employee':
            if employee:
                fed_to = employee.hr_id
            else:
                fed_to = None

        else:
           if employee:
                fed_to = employee.manager_id
           else:
                fed_to = None

        res=Feedback(id=str(uuid.uuid4()),fed_to=fed_to, fed_by=employee, fed_body=des, type='Feedback')
        res.save()
    
    return render(request, 'feedback.html', {'designation':request.session['designation'], 'name': request.session['name']})

@session_login_required
def ask_hr(request):
    if request.method == 'POST':   
        text=request.POST.get('query')
        employee = Employee.objects.get(id=request.session.get('id', None))
        hr=employee.hr_id
        # print(text, employee, hr)
        if hr is not None:
            res=askHR(id=str(uuid.uuid4()),text=text, hr_id = hr)
            res.save()
            return redirect("/employee")
        else:
            HttpResponse("The employee does not have a HR")
    return render(request,'askHR.html',{'designation':request.session['designation'], 'name': request.session['name']})

@session_login_required
def leave_request(request):
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        reason = request.POST.get('reason')
        type = request.POST.get('leavetype')

        employee = Employee.objects.filter(id = request.session.get('id', None)).first()
        mgr_id = employee.manager_id

        # Create and save a new LeaveRequest object
        if mgr_id is not None:
            new_leave_request = LeaveRequest(id=str(uuid.uuid4()),date_from=date_from, date_to=date_to, reason=reason, req_to = mgr_id, type=type)
            new_leave_request.save()
            if (request.session['designation']=='Manager'):
                return redirect("/manager")
            if (request.session['designation']=='Employee'):
                return redirect("/employee")
            if (request.session['designation']=='HR'):
                return redirect("/HR")
        else:
            HttpResponse("The employee does not have a Manager")    
    return render(request, 'leaverequest.html',{"designation":request.session['designation'], 'name': request.session['name']})

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
    
    return render(request,"profile.html", {"name":name,"password":password,"email":email,"address":address,"phone_number":phone_number, "designation":request.session['designation'],  'annual_leave': int(request.session['annual_leave']), 'casual_leave': int(request.session['casual_leave']), 'sick_leave': int(request.session['sick_leave'])})

@session_login_required
def view_pr(request):
    # Assuming you have stored the HR's ID in the session as 'hr_id'
    employee_id = request.session.get('id', None)

    if employee_id is not None:
        # Filter requests where req_to matches the logged-in HR's ID
        emp_requests = Feedback.objects.filter(fed_to=employee_id)

        return render(request, 'viewpr.html', {'emp_requests': emp_requests})
    else:
        # Handle the case where the HR is not logged in or the session is not set
        # You can redirect to a login page or handle it as per your application's logic.
        return render(request, 'mgr.html')
