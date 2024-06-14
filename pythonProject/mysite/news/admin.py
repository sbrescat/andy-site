from django.contrib import admin

# Register your models here.

from .models import Articles, Comments

admin.site.register(Articles)
admin.site.register(Comments)