from django.urls import path
from . import views

app_name = "vrisa"

urlpatterns = [
    path("", views.index, name="index"),
]
