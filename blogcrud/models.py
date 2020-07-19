from django.db import models

# Create your models here.
class Aurthor(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Blogs(models.Model):
    author = models.ForeignKey(Aurthor,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField(default=None)
    images = models.ImageField(default=None)
    content = models.TextField()

    def __str__(self):
        return self.title

