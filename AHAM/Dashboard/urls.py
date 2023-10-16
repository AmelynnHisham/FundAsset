from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('fund/<str:id>/', views.fundDetail, name='fundDetail'),
    path('transactions/', views.transactions, name='transactions'),
    path('allFunds/', views.allFunds, name='allFunds'),
    path('performance/', views.performance, name='performance'),
    path('addFund/<str:id>', views.addFund, name='addFund'),
]