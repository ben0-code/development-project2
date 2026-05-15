
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('transaction/', views.TransactionListCreateView.as_view()),
   path('transaction/<uuid:id>/', views.TransactionRetrieveUpdateDrstroyView.as_view())
]
