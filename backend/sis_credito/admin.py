from django.contrib import admin
from .models import CreditForm

class CreditFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'credit_api_response')
    readonly_fields = ('credit_api_response',)

admin.site.register(CreditForm, CreditFormAdmin)