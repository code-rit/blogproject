from django.db import models
from django.apps import apps
# Create your models here.

class Like(models.Model):
    likecount = models.IntegerField()
    dislikecount = models.IntegerField()


class Comment(models.Model):
    comments = models.TextField()
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    likes = models.ForeignKey(Like, on_delete=models.CASCADE)

class Category(models.Model):
    name  = models.CharField(max_length=50)
    code = models.CharField(max_length=20)

class Follower(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, default=None)

class Media(models.Model):
    '''reference will store the s3 bucket media base url reference'''
    reference = models.CharField()

class Notifications(models.Model):
    pass

class Article(models.Model):
    '''model to store data about article'''
    heading = models.CharField(max_length= 100)
    content = models.TextField()
    comments =models.ForeignKey(Comment, on_delete=models.CASCADE,default=None)
    likes = models.ForeignKey(Like, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.PROTECT)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    followers = models.ForeignKey(Follower, on_delete=models.CASCADE)
    notification = models .ForeignKey(Notifications, on_delete=models.CASCADE)
    
class UserProfile(models.Model):
    '''model for managing user data'''
    name =models.CharField(max_length=50)
    age = models.IntegerField()
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    



