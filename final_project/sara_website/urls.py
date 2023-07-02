
from django.urls import path
from . import views

urlpatterns = [
    #Default Views
    path("", views.index, name="Index"),
    path("dashboard/", views.dashboard, name="Dashboard"),

    #Functional Views
    path("add_carousel/", views.add_carousel, name="add_carousel"),
    path("add_description/", views.add_description, name="add_description"),
    path("add_paint/", views.add_paint, name="add_paint"),
    path("add_writing/", views.add_writing, name="add_writing"),

    #Dashboad add & delete buttons
    path("delete/<str:identifier>/<int:id>", views.delete_button, name="delete"),

    #Dashboard edit buttons
    path("edit/<str:identifier>/<int:id>", views.edit_button, name="edit"),

    #User views
    path("login/", views.login_view, name="login"),
]