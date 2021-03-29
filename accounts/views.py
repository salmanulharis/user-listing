from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        users = User.objects.all()
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'home.html', {'form':form, 'users':users})
    else:
        form = RegistrationForm()
        users = User.objects.all()
        return render(request, 'home.html', {'form':form, 'users':users})