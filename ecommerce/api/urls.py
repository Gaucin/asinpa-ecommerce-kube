
from django.urls import path

from ecommerce.api.views import OrdersView, OrderDetailView


urlpatterns = [
    path("orders/", OrdersView.as_view()),
    path("orders/<int:pk>/detail/", OrderDetailView.as_view()),
]
