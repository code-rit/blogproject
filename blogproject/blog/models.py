from django.db import models
from django.apps import apps
# Create your models here.

class Like(models.Model):
    likecount = models.IntegerField(null=True, blank=True)
    dislikecount = models.IntegerField(null=True, blank =True)


class Comment(models.Model):
    comments = models.TextField()
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, default = None)
    likes = models.ForeignKey(Like, on_delete=models.CASCADE, blank= True, null =True)

class Category(models.Model):
    name  = models.CharField(max_length=50)
    code = models.CharField(max_length=20)

class Follower(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, default=None)

class Media(models.Model):
    '''reference will store the s3 bucket media base url reference'''
    reference = models.CharField()

# The Notifications class is a model in Python that represents notifications.
class Notifications(models.Model):
    pass

class Article(models.Model):
    heading = models.CharField(max_length=100)
    content = models.TextField()
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, blank=True, null=True)
    likes = models.ForeignKey('Like', on_delete=models.CASCADE, blank=True, null=True)
    categories = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, null=True)
    media = models.ForeignKey('Media', on_delete=models.CASCADE, blank=True, null=True)
    followers = models.ForeignKey('Follower', on_delete=models.CASCADE, blank=True, null=True)
    notification = models.ForeignKey('Notifications', on_delete=models.CASCADE, blank = True, null=True)
    
class UserProfile(models.Model):
    '''model for managing user data'''
    name =models.CharField(max_length=50)
    age = models.IntegerField()
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, blank =True)
    



