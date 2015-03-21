from django.db import models


class Post(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=100)
    text = models.TextField()
    likes = models.IntegerField()
    shares = models.IntegerField()
    comments = models.ForeignKey("self", null=True)
