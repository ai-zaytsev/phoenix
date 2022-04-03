from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_at',
        'is_published',
    )
    list_display_links = (
        'title',
    )
    list_editable = ('is_published',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

