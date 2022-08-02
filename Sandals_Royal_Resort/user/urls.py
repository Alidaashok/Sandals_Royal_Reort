from django.urls import path
from . import views
urlpatterns=[
    path("booking",views.booking),
    path("check-in",views.check_in),
    path("check-out",views.check_out),
    path("complaint",views.complaint_posting),
    path("cuslogin",views.customer_login),
    path("feedback",views.feedback_posting),
    path("payment",views.payment),
    path("user-registration",views.user_registration)
]