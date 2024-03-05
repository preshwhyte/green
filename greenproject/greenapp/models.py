from django.db import models
from django.utils import timezone
from  django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    is_admin=models.BooleanField('is_admin',default=False)
    is_member=models.BooleanField('is_member',default=False)
    is_users=models.BooleanField('is_users',default=False)

class Volunteer(models.Model):
    full_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=100)
    cv=models.FileField(upload_to='cv/')
    comment=models.TextField()

class Contact(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=50)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class News(models.Model):
    photo=models.ImageField(blank=True, null=True, upload_to='news/photos/')
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    post=models.TextField()
    likes=models.ManyToManyField(CustomUser,default=False,blank=True,null=True, related_name='post_like')

    def __str__(self):
        return self.title

class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email







