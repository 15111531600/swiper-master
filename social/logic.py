import datetime

from user.models import User
from social.models import Swiped, Friend
from vip.logic import perm_require


def get_rcmd_user(user):
    ''' 获取推荐用户'''
    sex = user.profile.dating_sex
    location = user.profile.location
    min_age = user.profile.min_dating_age
    max_age = user.profile.max_dating_age

    current_year = datetime.date.today().year
    min_year = current_year - min_age
    max_year = current_year - max_age

    users = User.objects.filter(sex=sex, location=location,
                                birth_year__gte=max_year,
                                birth_year__lte=min_year)

    return users


def like(user, sid):
    '''喜欢一个用户'''
    Swiped.mark(user.id, sid, 'like')
    if Swiped.is_liked(sid, user.id):
        Friend.be_friends(user.id, sid)
        return True
    else:
        return False


@perm_require('superlike')
def superlike(user, sid):
    '''喜欢一个用户'''
    Swiped.mark(user.id, sid, 'superlike')
    if Swiped.is_liked(sid, user.id):
        Friend.be_friends(user.id, sid)
        return True
    else:
        return False


def dislike(user, sid):
    '''dislike'''
    Swiped.mark(user.id, sid, 'dislike')


@perm_require('rewind')
def rewind(user, sid):
    '''rewind'''
    try:
        # rewind 滑动记录
        Swiped.objects.get(uid=user.id, sid=sid).delete()
    except Swiped.DoesNotExist:
        pass

    Friend.break_off(user.id, sid)
