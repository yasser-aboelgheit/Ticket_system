from django.contrib import admin
from .models import Request

class RequestAdmin(admin.ModelAdmin):
    exclude=("owner","status","title","issue")
    readonly_fields=('owner',"status","title","issue",'slug' )
    include=("slug",)
    list_display = ('title','owner','employee', 'is_closed')

admin.site.register(Request,RequestAdmin)