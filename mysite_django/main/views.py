from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
def homepage(request):
    #return HttpResponse("wow, this is an <strong>dummy</strong> test")
    return render(request=request,
                  template_name="main/home.html",
                  context={'tutorials':Tutorial.objects.all})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username =  form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            # 这里可以跳转到某个特定页面写死的，，也可以跳转到某个app的某个name
            # 因为url可以是经常变化的
            return redirect("main:homepage")
        else:
            for msg, desc in form.error_messages.items():
                messages.error(request, f"{msg}:{desc}")
                print(msg, desc)
                
    # 失败重载这个页面
    form = NewUserForm
    return render(request,
                    "main/register.html",
                    context={'form':form})

def logout_request(request):
    logout(request)
    messages.info(request, f"Logout out successfully!")
    return redirect("main:homepage")

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('main:homepage')
            else:
                messages.error(request, 'Invalid Username or Password')
        else:
            messages.error(request, 'Invalid Username or Password')

    form = AuthenticationForm
    return render(request, "main/login.html", {'form':form})