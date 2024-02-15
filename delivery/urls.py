# delivery/urls.py

from django.urls import path
from .views import DeliveryCostAPIView

urlpatterns = [
    path('delivery_order', DeliveryCostAPIView.as_view(), name='delivery_order'),
    # Add more URL patterns for your views as needed
]
