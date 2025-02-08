from django.db import models

class BookModel(models.Model):
    GENRE_CHOICES = (
        ('FANTASY', 'FANTASY'),
        ('MYSTERY', 'MYSTERY'),
        ('ROMANCE', 'ROMANCE'),
    )
    image = models.ImageField(upload_to='films/', verbose_name='загрузите фото книги')
    title = models.CharField(max_length=100, verbose_name='укажите название книги')
    description = models.TextField(verbose_name='укажите описание книги', blank=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену книги', default=20)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='FANTASY',
                             verbose_name='укажите жанр книги')
    mail = models.CharField(max_length=100, verbose_name='укажите почту автора книги')
    author = models.CharField(max_length=100, verbose_name='укажите автора книги', default='Чингиз Айтматов')
    audio_book = models.URLField(verbose_name='укажите ссылку из YOUTUBE на аудиокнигу')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'