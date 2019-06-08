from django.contrib import admin
from .models import Order, OrderItem
from django.http import HttpResponse
import csv
import datetime
from django.urls import reverse
from django.utils.html import format_html

def OrderDetail(obj):
    return format_html('<a href="{}">Rozszerz</a>'.format(
        reverse('orders:AdminOrderDetail', args=[obj.id])
    ))


def ExportToCSV(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename=Order-{}.csv'.format(datetime.datetime.now().strftime("%d/%m/%Y"))
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%d/%m/%Y")
            data_row.append(value)
        writer.writerow(data_row)
    return response
    ExportToCSV.short_description = 'Export CSV'

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                     'email','address', 'postal_code', 
                     'city', 'updated', 'paid', OrderDetail]
    list_filter = ['created', 'updated', 'paid']
    inlines = [OrderItemInLine]
    actions = [ExportToCSV]

admin.site.register(Order, OrderAdmin)
