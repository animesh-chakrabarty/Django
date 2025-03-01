from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.save())
            return redirect("posts:feed")    
    else:
        form = UserCreationForm();        
    return render(request, 'users/register.html', {'form': form})

def login(request):
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("posts:feed")    
    else:
        form = AuthenticationForm();        
    return render(request, 'users/login.html', {'form': form})

def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("posts:feed")