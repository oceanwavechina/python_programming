from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def homepage(request):
    #return HttpResponse("wow, this is an <strong>dummy</strong> test")
    return render(request=request,
                  template_name="main/home.html",
                  context={'tutorials':Tutorial.objects.all})


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # 这里可以跳转到某个特定页面写死的，，也可以跳转到某个app的某个name
            # 因为url可以是经常变化的
            return redirect("main:homepage")
        else:
            for msg, desc in form.error_messages.items():
                print(msg, desc)
                
    # 失败重载这个页面
    form = UserCreationForm
    return render(request,
                    "main/register.html",
                    context={'form':form})