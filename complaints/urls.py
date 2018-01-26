from django.urls import path
from . import views

urlpatterns = [
    path('', views.ComplaintsListView.as_view(), name='complaint-list'),
    path('new/', views.ComplaintCreateView.as_view(), name='complaint-new'),
    path('<str:slug>/', views.ComplaintDetailView.as_view(), name='complaint-detail'),
    path('<str:slug>/edit/', views.ComplaintUpdateView.as_view(), name='complaint-edit'),
    path('<str:slug>/delete/', views.ComplaintDeleteView.as_view(), name='complaint-delete'),
]