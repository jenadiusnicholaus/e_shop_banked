from django.contrib import admin

from .models import Stock, StockItem

admin.site.register(Stock)

from django.db.models import Sum


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "stock",
        "qty",
        "unit_selling_price",
        "unit_estmated_profit",
        "total_estmated_profit",
        "total_selling_price",
        "status",
        "date_created",
    )


admin.site.register(StockItem, MemberAdmin)
