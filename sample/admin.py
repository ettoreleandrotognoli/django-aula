from django.contrib import admin
from .models import Movement

# Register your models here.
@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    search_fields = ('value', 'remark',)
    list_display = ('id', 'created', 'value', 'remark',)