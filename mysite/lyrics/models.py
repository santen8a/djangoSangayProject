from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100,blank=False, null=False) 
    text = models.CharField(max_length=250,blank=False, null=False)
    image = ImageField()
    # Just to give name to the object
    def __str__(self):
        return self.text
