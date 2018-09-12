from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=40)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.username


class Comment(models.Model):
    content = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="comment_author")
    likes = models.ManyToManyField(User, related_name="liked_comment_users")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content


class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name="liked_post_users")
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="post_author")
    pub_date = models.DateTimeField('date published')
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.title


