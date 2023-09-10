from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(
        null=False, auto_created=True, primary_key=True

    )
    title=models.CharField(max_length=225)
    shortDesc=models.TextField()
    body=models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=100)
    imgUrl = models.ImageField(
        upload_to='blogapp/static/images', blank=True, default='blogapp/static/images/blog-2-1000x600.jpg')