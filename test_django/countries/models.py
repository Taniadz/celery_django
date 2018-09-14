from django.db import models


# Create your models here.



class CountryManager(models.Manager):
    def create_country(self, id, name):
        country = self.create(id=id, name=name)
        return country

class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Name', max_length=200)
    objects = CountryManager()


