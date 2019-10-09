from django.db import models

from .constants import ICONS, ICONS_CHOICE


class Slide(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=400, verbose_name="Subtítulo")

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=400, verbose_name="Subtítulo")
    icon = models.CharField(max_length=20, choices=ICONS_CHOICE, default=ICONS.BOX,
        verbose_name='Ícone')

    def __str__(self):
        return self.title
