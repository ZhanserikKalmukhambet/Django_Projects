from django.urls import path

from . import views

urlpatterns = [
    path("<int:ind>", views.index, name="ind"),
    path("home/", views.home, name="home page"),
    path("create/", views.create, name="create a list")
]
