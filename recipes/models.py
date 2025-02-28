from django.db import models


class RecipeModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class IngredientModel(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=1)
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)