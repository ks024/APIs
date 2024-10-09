from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BookView.as_view(), name = 'book-list'),
    path('books/<int:pk>', views.SingleBookView.as_view(), name = 'view-book'),
]