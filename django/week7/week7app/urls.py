from django.urls import path
from week7app import views

urlpatterns = [
    path('insert', views.insert),
    path('companies', views.retrieveCompanyList),
    path('company/<id>/', views.retrieveCompanyDetail)
]
