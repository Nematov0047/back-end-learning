from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menuItemView'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='SingleMenuItemView'),
    path('ser/', views.ser, name='ser'),
]