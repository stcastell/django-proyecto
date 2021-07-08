from . import views
from django.urls import path

urlpatterns = [
	path('',views.index, name="index"),
	path('cart/<dato>/',views.cart, name="cart"),
]
