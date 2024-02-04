from django.db import models

class Sheep(models.Model):
    earing_number = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()

    def __str__(self):
        return self.earing_number