from django.db import models

# Create your models here.

class Todotable(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateTimeField()
    repeat=models.CharField(max_length=50)
    desc=models.TextField(max_length=500)

    def __str__(self):
        return self.name