from django.db import models


# Create your models here.
class Swiped(models.Model):
    STATUS = (
        ('superlike'),
        ('like'),
        ('dislike')
    )
    uid = models.IntegerField(verbose_name='mover id')
    sid = models.IntegerField(verbose_name='moved id')
    status = models.CharField(max_length=8, choices=STATUS)
    time = models.DateTimeField(auto_now_add=True)


class Friend(models.Model):
    uid = models.IntegerField()
    fid = models.IntegerField()