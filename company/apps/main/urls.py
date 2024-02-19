from django.urls import path,include
from .views import homepage,user_login

urlpatterns = [
    path('', homepage, name="homepage"),
    path('auth/', include('allauth.urls')),
]