from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):

    STATUS_CHOICES = [
        ('Criado', 'Criado'),
        ('Pendente', 'Pendente'),
        ('Feito', 'Feito')
    ]

    description = models.CharField(max_length=250)
    status = models.CharField(choices=STATUS_CHOICES, default='Criado', max_length=20)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.description, self.status, self.user_id
