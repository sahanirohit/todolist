from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    fm = UserCreationForm()
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm = UserCreationForm()
        return render(request, 'signup.html',{'signup_form':fm})
    
    return render(request, 'signup.html', {'signup_form':fm})