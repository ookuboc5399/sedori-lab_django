from django.views import View
from django.shortcuts import render, redirect
from accounts.forms import SignupUserForm
from allauth.account import views




class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/profile.html')

class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')

class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'
    form_class = SignupUserForm

class AccountView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/account.html')

class HowtouseView(View):
    template_name = 'accounts/howtouse.html'