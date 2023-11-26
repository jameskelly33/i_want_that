from django.contrib import admin
from django.urls import path
from . import views
from .views import delete_wish_list_item

urlpatterns = [
    path('jameslist', views.jameslist, name='jameslist'),
    path('orlalist', views.orlalist, name='orlalist'),
    path('jacklist', views.jacklist, name='jacklist'),
    path('flatlist', views.flatlist, name='flatlist'),
    path('add_to_wish_list', views.add_to_wish_list, name='add_to_wish_list'),
    path('delete/<int:item_id>/', delete_wish_list_item, name='delete_wish_list_item'),
]