from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)