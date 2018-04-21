from django.contrib import admin
from .models import Tenders, FavoriteTenders

class TendersAdmin(admin.ModelAdmin):
    list_display = ('etp', 'code', 'subject', 'customer', 'deadline')
    list_filter = ('etp',)
    search_fields = ('code', 'subject', 'customer')
    ordering = ['deadline']

admin.site.register(Tenders, TendersAdmin)
# admin.site.register(TenderDocuments)
admin.site.register(FavoriteTenders)
