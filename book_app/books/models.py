from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100,null=True,blank=True,default='')
    genre = models.CharField(max_length=100)
    read_on = models.DateTimeField(auto_now_add=True)
    page_count = models.IntegerField()
