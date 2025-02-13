from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Clothes(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=150)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'