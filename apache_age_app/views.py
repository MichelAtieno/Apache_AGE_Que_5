from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an error logging in. Try again."))
            return redirect('login')
    else:
        context = {

        }
    
        return render(request, 'registration/login.html', context)
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out."))

    return redirect('home')
    