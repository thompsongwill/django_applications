from django.shortcuts import render, redirect
from .forms import NewUserForm 

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('store/home')
    form = NewUserForm()
    return render(request, 'users/register.html', {'form':form})