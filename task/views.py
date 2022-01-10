from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    fm = UserCreationForm()
    return render(request, 'signup.html',{'signup_form':fm})