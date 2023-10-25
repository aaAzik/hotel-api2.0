from django.contrib import admin
from apps.book.models import *

@admin.register(Book)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)