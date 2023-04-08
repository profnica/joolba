from django.db import models

# Create your models here.

class SectionModel(models.Model):
    name = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class CategoryModel(models.Model):
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class SubCategoryModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name