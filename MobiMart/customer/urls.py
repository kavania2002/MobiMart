from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name="index"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("cart",views.cart,name="cart"),
    path("checkout",views.checkout,name="checkout"),
    path('logout',views.logout,name='logout'),
    path('updateItem',views.updateItem,name='updateItem'),
    path('processOrder',views.processOrder,name='processOrder')
]