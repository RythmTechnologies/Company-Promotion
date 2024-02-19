from django.shortcuts import render,redirect
from .mixin import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def homepage(request: HttpRequest) -> HttpResponse:
  return render(request, "index.html")



def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, "Username or Password is incorrect")
    return render(request, 'account/login.html')