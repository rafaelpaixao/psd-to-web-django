from django.contrib import admin

from .models import Slide, Card


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    pass


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass
