from django.urls import path
from .views import RatingView
from . import views

urlpatterns = [
    path('ratings', views.RatingsView.as_view()),
]

