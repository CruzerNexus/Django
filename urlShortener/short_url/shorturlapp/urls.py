from django.urls import path

from . import views
app_name = 'shorturlapp'
urlpatterns = [
    path('', views.submit_url, name='index'),
    path('submit_url', views.submit_url, name='submit_url'),
    path('<random_code>', views.short_url, name='short_url'),
]
