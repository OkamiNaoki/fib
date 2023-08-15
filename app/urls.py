from django.urls import path
from . import views

urlpatterns = [
    path("", views.FibonacciView.as_view(), name="fibonacci"),  # Use as_view() here
]