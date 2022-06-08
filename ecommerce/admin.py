from django.contrib import admin

from ecommerce.models import Order, OrderDetail


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "employee", "shipper", "order_date",)


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity",)
