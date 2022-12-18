from django.urls import path
from . import views
urlpatterns = [
    path('', views.TripListView.as_view(), name='home'),
    path('place/<int:pk>/', views.TripDetailView.as_view(), name='trip_detail_view'),
    path('create/', views.TripPlanCreate.as_view(), name='create_trip_plan')
]
