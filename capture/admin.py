from django.contrib import admin

# Register your models here.
from .models import categories, photos
# Register your models here.
admin.site.register(categories)
admin.site.register(photos)