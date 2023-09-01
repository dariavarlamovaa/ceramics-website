from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'