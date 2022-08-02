from django.urls import path
from . import views
urlpatterns=[
    path("",views.Admin_login),
    path("complaint",views.check_complaints),
    path("feedback",views.customer_feedback_view),
    path("room-approval",views.room_approval),
    path("room-reservation",views.Room_reservation_details),
    path("salary",views.salary_details),
    path("staffleave",views.staff_leave_approvals),
    path("staffdetails",views.staffdetails),
    path("payment",views.verify_payment)
]