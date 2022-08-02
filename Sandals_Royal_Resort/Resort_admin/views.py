from django.shortcuts import render

# Create your views here.
def Admin_login(request):
   return render(request,'Resort_admin/Admin_login.html')
def check_complaints(request):
    return render(request,'Resort_admin/check_complaints.html')
def customer_feedback_view(request):
    return render(request,'Resort_admin/customer_feedback_view.html')
def room_approval(request):
    return render(request,'Resort_admin/room_approval.html')
def Room_reservation_details(request):
    return render(request,'Resort_admin/Room_reservation_details.html')
def salary_details(request):
    return render(request,'Resort_admin/salary_details.html')
def staff_leave_approvals(request):
    return render(request,'Resort_admin/staff_leave_approvals.html')
def staffdetails(request):
    return render(request,'Resort_admin/staffdetails.html')
def verify_payment(request):
    return render(request,'Resort_admin/verify_payment.html')