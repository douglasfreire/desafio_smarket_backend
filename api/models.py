from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):

    STATUS_CHOICES = [
        ('Created', 'Created'),
        ('Progress', 'In Progress'),
        ('Done', 'Done')
    ]

    description = models.CharField(max_length=250)
    status = models.CharField(choices=STATUS_CHOICES, default='Created', max_length=20)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.description, self.status, self.user)
