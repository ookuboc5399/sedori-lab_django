from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='account_signup'),
    path('login/', views.LoginView.as_view(), name='account_login'),
    path('logout/', views.LogoutView.as_view(), name='account_logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('account/', views.AccountView.as_view(), name='account'),
    path('howtouse/', views.HowtouseView.as_view(), name='howtouse'),
]