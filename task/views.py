from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    fm = AuthenticationForm()
    if request.method == "GET":
        fm = AuthenticationForm()
        return render(request, 'login.html',{"login_form":fm})
    else:
        # if request.method == "POST":
        fm = AuthenticationForm(data=request.POST)
        if fm.is_valid():
            un = fm.cleaned_data.get('username')
            pw = fm.cleaned_data.get('password')
        user = authenticate(username = un, password = pw)
        if user is not None:
            return redirect('home')
        else:
            messages.add_message(request, "Invalid username and password. Try again...")
            return redirect('login')
    return render(request, 'login.html',{"login_form":fm})

def signup(request):
    fm = UserCreationForm()
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')
        
    else:
        fm = UserCreationForm()
        return render(request, 'signup.html',{'signup_form':fm})
    
    return render(request, 'signup.html', {'signup_form':fm})