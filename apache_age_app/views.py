from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import get_language, activate, gettext
from .forms import RegisterUserForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('apache_age_app:home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an error logging in. Try again."))
            return redirect('apache_age_app:login')
    else:
        context = {

        }
    
        return render(request, 'registration/login.html', context)
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out."))

    return redirect('apache_age_app:home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('apache_age_app:home')
    else:
        form = RegisterUserForm()
    context = {
        'form' : form,
    }
    return render(request, 'registration/register.html', context)
    