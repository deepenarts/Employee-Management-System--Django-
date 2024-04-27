from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("", login_page, name="login_page"),
    path("index/", index, name="index"),
    path("all_emp/", all_emp, name="all_emp"),
    path("add_emp", add_emp, name="add_emp"),
    path("remove_emp/", remove_emp, name="remove_emp"),
    path("remove_emp/<int:emp_id>", remove_emp, name="remove_emp"),
    path("filter_emp", filter_emp, name="filter_emp"),

    path("register/",register, name="register"),
    path ("logout/",logout_user, name="logout_user")
]
