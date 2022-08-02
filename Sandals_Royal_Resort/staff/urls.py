from django.urls import path
from . import views
urlpatterns=[
    path("leaverequest",views.leave_request),
    path("login",views.login),
    path("logout",views.Logout),
    path("resortbooking",views.resort_room_booking),
    path("availability",views.room_availability)

]