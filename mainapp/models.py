from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.TextField()
    category_image = models.ImageField(upload_to='category_images')


class Article(models.Model):
    title = models.TextField(blank=True)
    image = models.ImageField(upload_to='article_images')
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    reading_time = models.IntegerField()