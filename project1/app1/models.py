from django.db import models

# Create your models here.
class Emplyee(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    sal = models.FloatField()
    address = models.CharField(max_length=100)


    def __str__(self):
        return f'{eid}..{name}..{mail}...{sal}...{address}'
