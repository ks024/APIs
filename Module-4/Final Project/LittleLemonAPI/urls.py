from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('menu-items/', views.MenuItemListView.as_view(), name='menuitem-list'),
    path('menu-items/<int:pk>/', views.MenuItemDetailView.as_view(), name='menuitem-detail'),
    path('cart/menu-items/', views.CartView.as_view(), name='cart-view'),
]
