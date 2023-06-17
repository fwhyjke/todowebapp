from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.db.models import *
from django.urls import reverse

# Create your models here.


class ToDoIt(models.Model):
    user = ForeignKey(User, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    title = CharField(max_length=30, verbose_name='Задача')
    lvl = IntegerField(verbose_name='Уровень')
    description = TextField(blank=True, verbose_name='Описание')
    status = BooleanField(default=False)
    isfixed = BooleanField()
    end_at = DateTimeField(default=timezone.now)

    def __str__(self):
        return f'User {self.user}, task "{self.title}"'

    class Meta:
        verbose_name = 'Задачи пользователей'
        verbose_name_plural = 'Задачи пользователей'
