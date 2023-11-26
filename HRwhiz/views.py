from django.shortcuts import render, redirect
from employee.models import Employee
import random
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from functools import wraps
def session_login_required(function=None, session_key='id'):
    def decorator(view_func):
        @wraps(view_func)
        def f(request, *args, **kwargs):
            # print(request.session.keys())
            if session_key in request.session:
                return view_func(request, *args, **kwargs)
            return redirect('/')
        return f
    if function is not None:
        return decorator(function)
    return decorator

# Create your views here.
otp_dict = {}

def log_in(request):
    if request.method == 'POST':
        # Generate OTP
        #otp_secret = pyotp.random_base32()
       # otp = pyotp.TOTP(otp_secret)
        #otp_code = otp.now()
        otp_code=str(random.randint(100000, 999999))

        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = Employee.objects.get(email=email, password=password)
            
            if user is not None:
                # Store user data and OTP in the dictionary
                request.session['name'] = user.name
                request.session['id'] = user.id
                request.session['designation'] = user.designation
                request.session['sick_leave'] = user.sick_leave
                request.session['casual_leave'] = user.casual_leave
                request.session['annual_leave'] = user.annual_leave

                # Store the OTP in the dictionary
                otp_dict[user.id] = otp_code

                # Send the OTP via email
                subject = 'Your OTP for Login'
                message = f'Your OTP is: {otp_code}'
                from_email = 'hrwhizapp2023@gmail.com'  # Replace with your email
                recipient_list = [user.email]
                
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                # Redirect to OTP verification page
                return render(request, 'verify_otp.html')
                
        except Employee.DoesNotExist:
            return HttpResponse("Invalid email or password")

    return render(request, 'login.html')

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        user_id = request.session.get('id')
        
        if user_id in otp_dict:
            otp= otp_dict[user_id]
            # print(otp)
            if otp == entered_otp:
                designation = request.session.get('designation', None)
                # print(designation)
                # Updating the status of logged in user
                obj = Employee.objects.get(id=user_id)
                obj.status = True

                obj.save()
                
                if designation == "Employee":
                    return redirect('/employee')
                elif designation == "Manager":
                    return redirect('/manager')
                elif designation == "HR":
                    return redirect('/HR')

    return HttpResponse("Invalid OTP. Please try again.")

    

def log_out(request):
    obj = Employee.objects.get(id=request.session.get('id', None))
    obj.status = False

    obj.save()
    del request.session['name']
    del request.session['id']

    return redirect('/')