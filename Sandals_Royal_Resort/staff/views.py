from django.shortcuts import render

# Create your views here.
def leave_request(request):
    return render(request,'staff/leave_request.html')
def login(request):
    return render(request,'staff/login.html')
def Logout(request):
    return render(request,'staff/Logout.html')
def resort_room_booking(request):
    return render(request,'staff/resort_room_booking.html')
def room_availability(request):
    return render(request,'staff/room_availability.html')
