from django.contrib import admin


from account.models import Customer, Employee, Shipper


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_name", "address", "city", "postal_code", "country",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date",)


@admin.register(Shipper)
class ShipperAdmin(admin.ModelAdmin):
    list_display = ("name", "phone",)
