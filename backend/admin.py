from django.contrib import admin
from .models import *

admin.site.register(Users)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Programlist)

admin.site.register(DietCategory)
admin.site.register(DietSubCategory)
admin.site.register(DietProgramlist)
