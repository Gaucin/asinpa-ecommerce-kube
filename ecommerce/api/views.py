from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView

from ecommerce.api.serializers import OrderSerializer, OrderDetailSerializer
from ecommerce.models import Order, OrderDetail


class OrdersView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(RetrieveAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer(many=True)

    def filter_queryset(self, queryset):
        order_id = self.kwargs["pk"]
        queryset = OrderDetail.objects.filter(order=order_id)
        return super().filter_queryset(queryset)
