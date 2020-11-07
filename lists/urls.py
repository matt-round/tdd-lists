from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from lists.views import view_list, new_list, add_item

urlpatterns = [
    path('<int:list_id>/', view_list, name='view_list'),
    path('<int:list_id>/add_item', add_item, name='add_item'),
    path('new', new_list, name='new_list'),
]
