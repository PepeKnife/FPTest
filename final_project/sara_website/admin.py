from django.contrib import admin
from .models import User, abt_description, abt_carousel, writings, paints

class descriptionView(admin.ModelAdmin):
    list_display = ("id",)
class carouselView(admin.ModelAdmin):
    list_display = ("id", "num", "owner", "text")
class writingsView(admin.ModelAdmin):
    list_display = ("id", "name", "text")
class paintView(admin.ModelAdmin):
    list_display = ("id", "name")

# Register your models here.
admin.site.register(User)
admin.site.register(abt_description, descriptionView)
admin.site.register(abt_carousel, carouselView)
admin.site.register(writings, writingsView)
admin.site.register(paints, paintView)