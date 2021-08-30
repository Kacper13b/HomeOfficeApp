from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.author.username + " home office request"
