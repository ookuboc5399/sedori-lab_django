from django.urls import path
from api_ebay_circle import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index_detail', views.IndexDetailView.as_view(), name='index_detail'),
    path('ebay_detail', views.EbayDetailView.as_view(), name='ebay_detail'),
    path('kokunai_detail', views.KokunaiDetailView.as_view(), name='kokunai_detail'),
    path('amazonoem_detail', views.AmazonoemDetailView.as_view(), name='amazonoem_detail'),
    path('import_detail', views.ImportDetailView.as_view(), name='import_detail'),
    path('cource/', views.CourceView.as_view(), name='cource'),
    path('ebay_circle/', views.EbaycircleView.as_view(), name='ebay_circle'),
    path('contact/', views.CONTACTView.as_view(), name='contact'),
    path('question/', views.QUESTIONView.as_view(), name='question'),
    path('privacy/', views.PRIVACYView.as_view(), name='privacy'),
    path('create-checkout-session/', views.create_checkout_session, name='checkout_session'),
    path('success/', views.PaymentSuccessView.as_view(), name='success'),
    path('cancel/', views.PaymentCancelView.as_view(), name='cancel'),
    path('checkout/', views.PaymentCheckoutView.as_view(), name='checkout'),
]