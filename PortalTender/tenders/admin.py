from django.contrib import admin
from .models import RzdTenders, Tenders, TenderDocuments

admin.site.register(RzdTenders)
admin.site.register(Tenders)
admin.site.register(TenderDocuments)

