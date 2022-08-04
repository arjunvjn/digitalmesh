from django.urls import path
from .views import *

urlpatterns = [
    path('index/',home,name='index'),
    path('create-task/',create_todo,name='create-task'),
    path('update-task/<int:id>/',update_todo,name='update-task'),
    path('ajax-delete-task',delete_todo,name='ajax-delete-task'),
    path('filter_repeat/',filter_repeat,name='filter_repeat'),
    path('search_todo/',search_todo,name='search_todo')
]