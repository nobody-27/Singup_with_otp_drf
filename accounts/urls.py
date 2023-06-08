from django.contrib import admin
from django.urls import path
from accounts.views import RegisterApi,Verify_Otp,Upload_Docs
urlpatterns = [
    path('register/',RegisterApi.as_view(),name="register"),
    path('verify_otp/',Verify_Otp.as_view(),name="verify_otp"),
    path('upload_docs/',Upload_Docs.as_view(),name="upload_docs")
]
