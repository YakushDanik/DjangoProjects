from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LogInForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration was successful!")
            return(redirect('home'))
    else:
        form = SignUpForm()
    return render(request, "user/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LogInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You're logged in as {username}")
                return redirect("home")
            else:
                messages.error(request, "Invalid ussername of password")
        else:
            messages.error(request, "Invalid ussername of password")
    else:
        form = LogInForm()
    return render(request, "user/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You've logged out")
    return redirect("home")