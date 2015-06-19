import datetime

from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title       #methods analogous to the toString() method in a Java

class LiquorStore(models.Model):
    name = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=128)
    lat = models.CharField(max_length=64, blank=True)
    lon = models.CharField(max_length=64, blank=True)
    storetype = models.CharField(max_length=64, blank=True)

    def __unicode__(self):
        return self.name
