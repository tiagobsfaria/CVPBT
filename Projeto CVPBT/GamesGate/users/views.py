from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterUserForm, EditProfileForm, ChangePasswordForm, EditProfileImageForm
from .models import Account

# Create your views here.


def login_user(request):
    if request.method=='POST':
        username = request.POST['usernamelogin']
        password = request.POST['passwordlogin']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error Logging In, Try Again..."))
            return redirect('login')

    else:
        return render(request,'authenticate/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("Logged out successfully!"))
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            account = Account.objects.create(user=user)

            # Check if a profile picture was uploaded
            if 'profile_picture' in request.FILES:
                account.profile_image = request.FILES['profile_picture']
            else:
                # Assign a predefined profile picture path
                account.profile_image = 'images/profile/predefined.jpg'

            account.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register.html', {'form': form})


def user_data(request):
    return render(request, 'authenticate/user_information.html')


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'authenticate/edit_profile.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'authenticate/change_password.html', {'form': form})


@login_required(login_url='login')
def edit_profile_image(request):
    if request.method == 'POST':
        form = EditProfileImageForm(request.POST, request.FILES, instance=request.user.account)
        if form.is_valid():
            # Save the new profile image without deleting the old one
            account = form.save(commit=False)

            # Check if a new profile image was uploaded
            new_image = form.cleaned_data.get('profile_image')
            if new_image:
                # Update the profile image field with the new image
                account.profile_image = new_image

            # Save the account instance
            account.save()

            messages.success(request, "Profile Image updated successfully")
            return redirect('home')
    else:
        form = EditProfileImageForm(instance=request.user.account)

    return render(request, 'authenticate/profile_image_edit.html', {'form': form})

