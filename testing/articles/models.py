from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add thumbnail later
    # add in author later
    # strring object of this articles

    def __str__(self):
        return self.title

    # creating a model method

    def snippet(self):
        return self.body[:50] + '...'
