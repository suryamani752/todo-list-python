from django.urls import path
from todoapp import views

urlpatterns = [
    path('main', views.index, name='index'),
    path('delete/<str:pk>', views.delete,name='delete'),
    path('load-more-todos/', views.index, name='load-more-todos'), 
    
]