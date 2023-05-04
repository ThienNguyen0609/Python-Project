from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name='home'),
    path("detail/<int:id>", views.Detail, name="detail"),
    path("cart/", views.Cart, name="cart"),
    path("update_item/", views.updateItem, name="update_item"),
    path("inc_dec_item/", views.Inc_Dec_Item, name='inc_item'),
    path('test/', views.Test, name='test'),
]