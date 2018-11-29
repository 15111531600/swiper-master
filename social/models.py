from django.db import models


class Swiped(models.Model):
    '''滑动记录'''
    STATUS = (
        ('superlike', '超级喜欢'),
        ('like', '喜欢'),
        ('dislike', '不喜欢'),
    )

    uid = models.IntegerField(verbose_name='滑动者的 UID')
    sid = models.IntegerField(verbose_name='被滑动者的 UID')
    status = models.CharField(max_length=8, choices=STATUS)
    time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def mark(cls, uid, sid, status):
        '''标记一次滑动'''
        if status in ['superlike', 'like', 'dislike']:
            cls.objects.create(uid, sid, status)

    @classmethod
    def is_liked(cls, uid, sid):
        '''检查是否喜欢过某人'''
        return cls.objects.filter(uid=uid, sid=sid,
                                  status__in=['like', 'superlike']).exists()


class Friend(models.Model):
    '''好友'''
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def be_friends(cls, uid1, uid2):
        pass