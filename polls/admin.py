from django.contrib import admin
from .models import Memo

# Register your models here.
@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin) :
    list_display= ['title', 'content', 'is_important', 'created_at']
    list_display_links=['title']