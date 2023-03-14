from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        ROCK = 'ROCK'
        ALTERNATIVE = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    class Type(models.TextChoices):
        DISQUES = 'Records'
        VETEMENTS = 'Clothing'
        POSTERS = 'Posters'
        DIVERS = 'Misc'

    title = models.fields.CharField(max_length=100)
    type = models.fields.CharField(choices=Type.choices, max_length=50)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True, blank=True)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
