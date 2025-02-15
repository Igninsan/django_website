from django.db import models
from books.models import BookModel


class CartModel(models.Model):
    choice_book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

