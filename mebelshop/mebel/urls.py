from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:slug_category>', views.shop, name='category_view'),
    path('design/', views.design, name='design'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('thank-you/', views.thank_you, name='thank-you'),
    path('wrong/', views.wrong, name='wrong'),
]
