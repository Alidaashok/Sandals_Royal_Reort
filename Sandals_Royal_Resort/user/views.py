from django.shortcuts import render

# Create your views here.
def booking(request):
    return render(request,'user/booking.html')
def check_in(request):
    return render(request,'user/check_in.html')
def check_out(request):
    return render(request,'user/check-out.html')
def complaint_posting(request):
    return render(request,'user/complaint_posting.html')
def customer_login(request):
    return render(request,'user/customer_login.html')
def feedback_posting(request):
    return render(request,'user/feedback_posting.html')
def payment(request):
    return render(request,'user/payment.html')
def user_registration(request):
    return render(request,'user/user_registration.html')
