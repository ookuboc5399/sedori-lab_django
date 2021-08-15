from django.urls import path
from api_ebay_circle import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ebay/', views.EbayView.as_view(), name='ebay'),
]