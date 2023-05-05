from django.db import models
from django.db.models import *
from django.urls import reverse

# Create your models here.


class ToDoIt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = IntegerField()
    title = CharField(max_length=40, verbose_name='Задача')
    description = TextField(blank=True, verbose_name='Описание')
    status = BooleanField(default=False)

    def __str__(self):
        return f'User {self.user}, task "{self.title}"'

    class Meta:
        verbose_name = 'Задачи пользователей'
        verbose_name_plural = 'Задачи пользователей'
