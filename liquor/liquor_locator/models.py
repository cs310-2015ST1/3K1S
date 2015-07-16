import datetime
import math
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class LiquorStoreManager(models.Manager):
    def near(self, latitude, longitude, radius):
        unit = 6371

        from django.db import connection, transaction

        cursor = connection.cursor()
        connection.connection.create_function('acos', 1, math.acos)
        connection.connection.create_function('cos', 1, math.cos)
        connection.connection.create_function('radians', 1, math.radians)
        connection.connection.create_function('sin', 1, math.sin)
        connection.connection.create_function('float', 1, float)

        sql = """SELECT *, (acos(sin(radians(%f)) * sin(radians(float(lat))) + cos(radians(%f)) 
        * cos(radians(float(lat))) * cos(radians(%f-float(lon)))) * %d)
        AS distance FROM liquor_locator_LiquorStore WHERE distance < %f 
        ORDER BY distance;""" % (latitude, latitude, longitude, unit, radius)

        cursor.execute(sql)
        ids = [row[0] for row in cursor.fetchall()]
        return self.filter(id__in=ids)

class LiquorStore(models.Model):
    name = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=128)
    lat = models.CharField(max_length=64, blank=True)
    lon = models.CharField(max_length=64, blank=True)
    storetype = models.CharField(max_length=64, blank=True)
    hours = models.CharField(max_length=300, blank=True)
    storeHash = models.CharField(max_length=32, blank=True)
    phone = models.CharField(max_length=32, blank=True)

    objects = LiquorStoreManager()

    fav_user = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    user=models.OneToOneField(User)
    comment = models.CharField(max_length=128)
    isAnon = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    liquorStore = models.ForeignKey(LiquorStore, null=True)
    user = models.ForeignKey(User, null=True)
    
    def __unicode__(self):
        return self.comment

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

# class Comment (models.Model):
#     liquorStore = models.ForeignKey(LiquorStore)

#     when a liquorstore is selected, you can filter liquorstore specific comments from all comments and display that

# class LiquorStore (models.Model):
#     user = models.ManyToMany(UserProfile)

# class UserProfile (modles.Model):
#     user = models.OneToOneField(User)
