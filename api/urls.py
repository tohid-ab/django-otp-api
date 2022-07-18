from django.urls import include, path
from rest_framework import routers
from .views import OTPView


urlpatterns = [
    path('otp', OTPView.as_view(), name='otp_view')
]