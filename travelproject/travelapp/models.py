from django.db import models

# Create your models here.
class Destination(models.Model):
    dest_name = models.CharField(max_length=250)
    dest_image = models.ImageField(upload_to='pics')
    dest_description = models.TextField()

    def __str__(self):
        return self.dest_name

class Teams(models.Model):
    member_name = models.CharField(max_length=50)
    member_image = models.ImageField(upload_to='pics')
    member_description = models.TextField()

    def __str__(self):
        return self.member_name
