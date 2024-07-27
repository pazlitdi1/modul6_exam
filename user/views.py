from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import FormView, CreateView


class LoginView(FormView):
    template_name = 'auth/login.html'
    form_class = AuthenticationForm
    success_url = '/home/'  # Home page URL

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            return render(request, 'auth/register.html', {'message_password': 'Error password'})

        if User.objects.filter(username=username).exists():
            return render(request, 'auth/register.html', context={"message": "Already registered"})

        new_user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        new_user.set_password(password)
        new_user.save()
        return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
