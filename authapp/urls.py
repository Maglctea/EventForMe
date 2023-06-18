from django.urls import path, include
from authapp.views import GoogleLogin
from authapp.views import ProfileVendorView, ProfileClientView

app_name = 'authapp'

urlpatterns = [
    path('profile_client/', ProfileClientView.as_view(), name='profile_client'),
    path('profile_vendor/', ProfileVendorView.as_view(), name='profile_view'),
    path('google/', GoogleLogin.as_view(), name='google_login'),

]
