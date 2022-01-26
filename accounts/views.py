from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from social.models import MyProfile

# Custom imports
from .forms import CreateUserForm
from .decorators import unauthenticated_user


# Create your views here.

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 'accounts/login.html')

    context = {}
    return render(request, 'accounts/login.html', context)


@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # MyProfile.objects.create(
            #     user=user,
            #     name=user.username,
            #     email=user.email
            # )
            
            print("USER CREATER: ", username)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        else:
            messages.warning(request, 'Invalid Details')
            context = {'form': form}
            return render(request, 'accounts/registration_form.html', context)
    context = {'form': form}
    return render(request, 'accounts/registration_form.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

