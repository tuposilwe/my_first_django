from django.contrib import admin
from .models import App, Person

admin.site.register(Person)

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_verified', 'uploadDate', 'priority')
    # Note: search_fields must be a list or tuple. Added a comma below:
    search_fields = ('title',) 
    list_filter = ('priority', 'uploadDate')


