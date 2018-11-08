from django.contrib import admin
from .models import NewsUser

# Register your models here.

@admin.register(NewsUser)
class NewsUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added', 'is_active')
    search_fields = ('email',)