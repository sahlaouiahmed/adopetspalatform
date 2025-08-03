from django.contrib import admin
from .models import Pet, AdoptionRequest
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Pet)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'species', 'breed', 'age' , 'posted_by')
    search_fields = ['species']
    list_filter = ('species','posted_at',)
    prepopulated_fields = {'name': ('name',)}
    summernote_fields = ('description',)
# Register your models here.
admin.site.register(AdoptionRequest)
