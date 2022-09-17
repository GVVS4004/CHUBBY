from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.navigateForm, name="upload"),
    path('delete/<int:id>', views.deleteFood, name="delete-food"),
    path('edit/<int:id>', views.updateFood, name="update-food"),
    path('push-data/', views.pushData, name="push-data"),
]