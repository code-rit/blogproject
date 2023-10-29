from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

@register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Like._meta.fields]

@register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Comment._meta.fields]

@register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Category._meta.fields]

@register(Follower)
class FollowersAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Follower._meta.fields]

@register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Media._meta.fields]

@register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Notifications._meta.fields]

@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Article._meta.fields]

@register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in UserProfile._meta.fields]
