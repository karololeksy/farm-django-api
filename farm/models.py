from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField

class Sex(ChoiceEnum):
    empty = "Empty"
    male = "Male"
    female = "Female"


class Sheep(models.Model):
    earing_number = models.CharField(max_length=50)
    sex = EnumChoiceField(enum_class=Sex, default=Sex.empty)
    date_of_birth = models.DateField()
    breed = models.CharField(max_length=50)
    in_program = models.BooleanField()


    def __str__(self):
        return self.earing_number