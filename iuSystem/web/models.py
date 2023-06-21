from django.db import models

from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Participant(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profile-pics/")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=9)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=8)
    category = models.CharField(max_length=100)
    name_of_school = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    date_registered = models.DateTimeField(auto_now=True)
    reference = models.CharField(max_length=20)
    completed =  models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.first_name + ' ' + self.last_name}'s Profile"
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
        
    #     img = Image.open(self.profile_image.url
    #                      )
        
    #     # resize image if image size is greater than 50% height and width
    #     if img.height > 50 or img.width > 50: complete! Reference: FavourBamgboye6699
    #         # define size to resize images
    #         size = (50, 50)
    #         img.thumbnail(size)
    #         # save image
    #         img.save(self.profile_image.path, quality=100)
    #         img.close()
    #         self.profile_image.close()
    
    @property
    def fullname(self):
        return f"{self.first_name, self.last_name}"
