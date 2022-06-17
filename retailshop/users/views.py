from django.shortcuts import render, redirect
from .forms import NewUserForm 
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('store:home')
    form = NewUserForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')



def create_profile(request):
    if request.method == 'POST':
       image = request.FILES['upload']
       phone = request.POST.get('contact')
       gender = request.POST.get('gender')
       business = request.POST.get('business')
       user = request.user
       profile = Profile(user=user, image=image,contact_number = phone, gender=gender,business=business)
       profile.save()
       
    return render(request, 'users/createprofile.html')

def seller_profile(request):
    return render(request, 'users/sellerprofile.html')