from django.urls import path
from . import views

urlpatterns = [
    path('<str:text>', views.MachineView.as_view()),
]