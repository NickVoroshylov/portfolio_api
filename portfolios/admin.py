from django.contrib import admin

from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_display = ('owner', 'name', 'created')


admin.site.register(Portfolio, PortfolioAdmin)
