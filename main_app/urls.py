from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('cars/', views.cars_index, name='index'),
 path('cars/<int:car_id>/', views.cars_detail, name='detail'),
 path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
 path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
 path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
 path('cars/<int:car_id>/add_mods/', views.add_mods, name='add_mods'),
 path('shop/', views.ShopList.as_view(), name='shop_index'),
  path('shop/<int:pk>/', views.ShopDetail.as_view(), name='shop_detail'),
  path('shop/create/', views.ShopCreate.as_view(), name='shop_create'),
  path('shop/<int:pk>/update/', views.ShopUpdate.as_view(), name='shop_update'),
  path('shop/<int:pk>/delete/', views.ShopDelete.as_view(), name='shop_delete'),
  path('cars/<int:car_id>/assoc_shop/<int:shop_id>/', views.assoc_shop, name='assoc_shop'),
]