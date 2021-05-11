from django.contrib import admin
from django.urls import path
from myapp import views



urlpatterns = [
    path("",views.index,name="myapp"),
    path("signup",views.Signup,name="myapp"),
    path("login",views.Login,name="myapp"),
    path("cart",views.Cart,name="myapp"),
    path("logout",views.logout,name="myapp"),
   

]