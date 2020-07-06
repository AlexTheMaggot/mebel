from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:slug_category>', views.shop, name='category_view'),
    path('design/', views.design, name='design'),
    path('about/', views.about , name='about'),
    path('contact/', views.contact, name='contact'),
]
