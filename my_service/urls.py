from django.urls import path
from .views import statistics, vehicles, vehicle, MyOrders, MyOrder, search

urlpatterns = [
    path('', statistics, name='statistics'),
    path('vehicles/', vehicles, name='vehicles'),
    path('vehicle/<int:vehicle_id>', vehicle, name='vehicle'),
    path('orders/', MyOrders.as_view(), name='orders'),
    path('order/<int:pk>', MyOrder.as_view(), name='order'),
    path('search/', search, name='search')
]