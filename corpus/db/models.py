from djongo import models

class SubCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    subcategory = models.ArrayModelField(
        model_container=SubCategory
    )
    def __str__(self):
        return self.name
