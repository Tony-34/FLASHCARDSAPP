# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.shortcuts import render

# from django.contrib.auth.decorators import login_required


# @login_required(login_url='/accounts/login/')
# def article(request, article_id):


from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/register.html', context)


@login_required(login_url='/accounts/login/')
def profile(request):
    projects = Projects.objects.all()
    posts = Profile.objects.all()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'user_form':user_form,
    'profile_form':profile_form,
    'posts':posts,
    'projects':projects,
    }
    return render(request, 'profile/profile.html', context)

@login_required(login_url='/accounts/login/')
def updateprofile(request):
    projects = Projects.objects.all()
    posts = Profile.objects.all()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'user_form':user_form,
    'profile_form':profile_form,
    'posts':posts,
    'projects':projects,
    }

    return render(request, 'profile/update_profile.html', context)
