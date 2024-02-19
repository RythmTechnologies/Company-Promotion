from django.urls import path
from .views import site_blog, site_single_blog


urlpatterns = [
    path('', site_blog, name="main-blog"),
    path('<slug>', site_single_blog, name="single-blog"),

]