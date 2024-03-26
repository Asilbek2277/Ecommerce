from django.db import models

class Country(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name


class City(models.Model):
    name=models.CharField(max_length=255)
    country=models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='categories/')
    def __str__(self):
        return  self.name

class Subcategory(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='subcategories/', blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




