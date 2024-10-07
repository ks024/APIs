from django.urls import path
# from .views import RatingsView
from . import views

urlpatterns = [
    # path('ratings', views.RatingsView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]

