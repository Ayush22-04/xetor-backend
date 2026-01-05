from django.contrib import admin
from .models import Category, Product, HomeHero, ContactMessage

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(HomeHero)
admin.site.register(ContactMessage)
