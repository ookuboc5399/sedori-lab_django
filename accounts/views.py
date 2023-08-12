from django.views import View
from django.shortcuts import render, redirect
from accounts.forms import SignupUserForm
from allauth.account import views
from .models import CustomUser



# class ProfileView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'accounts/profile.html')

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
        profile_data = CustomUser.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]
        return render(request, 'accounts/account.html', {
            'profile_data': profile_data,
        })

class HowtouseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/howtouse.html')

class MypageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/mypage.html')