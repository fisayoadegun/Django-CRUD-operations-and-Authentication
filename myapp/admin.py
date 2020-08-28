from django.contrib import admin
from myapp.models import Flower, Category,Tag

# Register your models here.
admin.site.register(Flower)
admin.site.register(Category)
admin.site.register(Tag)
