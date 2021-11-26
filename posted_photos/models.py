from django.db import models
from django.utils import timezone
import datetime as dt

class Category(models.Model):
    category_name = models.CharField(max_length = 60)

    def __str__(self):
        return self.category_name
    
    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

class Location(models.Model):
    location_name = models.CharField(max_length = 60)
    
    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.location_name
    
    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id = id).update(image = value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', default='default.jpg')
    name = models.CharField(max_length = 60)
    description = models.TextField()
    author = models.CharField(max_length = 40)
    date_posted = models.DateTimeField(default = timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,)

    @classmethod
    def filter_by_location(cls, location):
        location_image = Image.objects.filter(location__location_name=location).all()
        return location_image

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image = value)
    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id = id).all()
        return image
    
    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(name__icontains=category)
        return images
    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    class Meta:
        ordering = ['date_posted']