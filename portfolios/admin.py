from django.contrib import admin

from .models import Portfolio, Picture


class PortfolioAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_display = ('owner', 'name', 'created')


class PictureAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_display = ('portfolio', 'name', 'created')


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Picture, PictureAdmin)
