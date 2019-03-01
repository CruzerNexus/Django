from django.urls import path

from . import views
app_name = 'grocerylist'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add_item'),
    path('delete/<int:pk>', views.delete_item, name='delete_item')
]
