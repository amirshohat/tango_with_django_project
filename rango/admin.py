from django.contrib import admin
from rango.models import Category, Page, UserProfile



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page,AuthorAdmin)
admin.site.register(UserProfile)
