from django.urls import path
from . import views
criRapp = 'my_criR'

urlpatterns = [
    path('', views.CrirListView.as_view(), name='home'),
    path('cri/<int:pk>/', views.CrirDetailView.as_view(), name='cri_detail'),
    path('cri/new/', views.CrirCreateView.as_view(), name='cri_new'),
    path('cri/<int:pk>/edit/', views.CrirUpdateView.as_view(), name='cri_edit'),
    path('cri/<int:pk>/delete', views.CrirDeleteView.as_view(), name='cri_delete'),
]
