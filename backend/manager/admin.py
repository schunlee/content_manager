from django.contrib import admin

# Register your models here.
from .models import Clerk, Country, ClerkType, BusinessGroup, Article, Customer


@admin.register(Clerk)
class ClerkAdmin(admin.ModelAdmin):
    list_display = ('clerk_number', 'note')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')


@admin.register(ClerkType)
class ClerkTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(BusinessGroup)
class BusinessGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.get_fields()]
