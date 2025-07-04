from django.contrib import admin
from website.models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('id', 'name', 'created_date',)
    search_fields = ('id', 'name', 'email', 'subject')
    list_filter = ('email', )