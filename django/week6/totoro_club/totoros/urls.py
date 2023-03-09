from django.urls import path
from totoros import views

urlpatterns = [
    # path('template/', views.template),
    path('', views.index),
    path('create/', views.create),
    path('read/<name>/', views.read)
]
