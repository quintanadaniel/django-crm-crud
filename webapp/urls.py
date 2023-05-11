from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name=""),
    path("register", views.register, name="register"),
    path("my-login", views.login, name="my-login"),
    path("user-logout", views.logout, name="user-logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("create-record", views.create_record, name="create-record"),
    path("update-record/<int:pk>", views.update_record, name="update-record"),
    path("delete-record/<int:pk>", views.delete_record, name="delete-record"),
    path("record/<int:pk>", views.view_record, name="record"),
]
