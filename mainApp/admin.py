from django.contrib import admin

from .models import *

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Subcategory)
