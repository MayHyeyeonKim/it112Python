from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('detail/<int:id>/', views.detail, name='detail'),
    # path('student/<int:id>/', views.detail, name='student'),
    # path('student/', views.students, name='all_students'),
    # path('student/<int:id>/', views.detail, name='student'),

]