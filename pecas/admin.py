
# pecas/admin.py
from django.contrib import admin
from .models import Peca

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor')
    search_fields = ('nome',)
    list_filter = ('nome',)