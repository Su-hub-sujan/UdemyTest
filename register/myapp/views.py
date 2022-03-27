from django.shortcuts import render
from .models import*
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    registered=False

    if request.method == 'POST':

        user_form=UserForm(request.POST)
        profile_form=UserProfile(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=True)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True

    else:
        user_form=UserForm()
        profile_form=UserProfile()

    return render(request,'registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered
                   })
