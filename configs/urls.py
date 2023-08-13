from django.urls import path

from cars.views import CarListCreateView, CarUpdateDestroyView

urlpatterns = [
    path('cars', CarListCreateView.as_view()),
    path('cars/<int:pk>', CarUpdateDestroyView.as_view())
]
