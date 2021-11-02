from django.db import models
from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = "Комнаты"

    def __str__(self):
        return f"{self.name}"


class Message(models.Model):
    value = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=250, default='support')
    room = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"{self.value}"


class NotAuthUsersMessage(models.Model):
    value = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Сообщение незарегестрированного пользователя'
        verbose_name_plural = "Сообщения незарегестрированных пользователей"

    def __str__(self):
        return f"{self.value}"