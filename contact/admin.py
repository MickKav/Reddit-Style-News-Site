from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = (
        ('created_date', DateRangeFilter),
        'user',
        'name',
        'email',
        'phone',
     )

    list_display = (
        'message_id',
        'user',
        'name',
        'message',
        'phone',
        'created_date',
     )

    search_fields = ['name']
