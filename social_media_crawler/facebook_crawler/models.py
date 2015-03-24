from django.db import models

# Create your models here.


class Post(models.Model):
    graph_id = models.CharField(max_length=50)
    date = models.DateTimeField()
    name = models.CharField(max_length=100)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    replyto = models.ForeignKey("self", null=True)
