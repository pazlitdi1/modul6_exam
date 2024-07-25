from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required()
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


@login_required()
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            return render(request, 'auth/register.html', {'message_password': 'Error password'})

        else:

            if User.objects.filter(username=username).exists():
                return render(request, 'auth/register.html', context={"message": "Already registered"})
        new_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        return redirect('login')

    return render(request, 'auth/register.html')


def logout_view(request):
    logout(request)
    return redirect('login')
