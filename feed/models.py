from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Request(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #8 home office days every month
    date_from = models.DateField()
    date_to = models.DateField()
    working_days_off = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(8)])
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.author.username + " home office request"
