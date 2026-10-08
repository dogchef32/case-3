from django.db import models

class Visitor(models.Model):
    name = models.CharField('Имя', max_length=100)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return self.name
