from django.contrib import admin
from .models import Blog, Label, Category

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Label)
