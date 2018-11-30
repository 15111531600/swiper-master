from lib.http import render_json

from social import logic
from social.models import Friend


# Create your views here.
def get_user(request):
    '''get user list'''
    group_num = int(request.GET.get('group_num', 0))
    start = group_num * 5
    end = start + 5
    users = logic.get_rcmd_user(request.user)[start:end]

    result = [user.to_dict() for user in users]
    return render_json(result)


def like(request):
    '''like'''
    sid = int(request.POST.get('sid'))
    is_matched = logic.like(request.user, sid)
    return render_json({'is_matched': is_matched})


def superlike(request):
    '''superlike'''
    sid = int(request.POST.get('sid'))
    is_matched = logic.superlike(request.user, sid)
    return render_json({'is_matched': is_matched})


def dislike(request):
    '''dislike'''
    sid = int(request.POST.get('sid'))
    logic.dislike(request.user, sid)
    return render_json(None)


def rewind(request):
    '''rewind'''
    sid = int(request.POST.get('sid'))
    logic.rewind(request.user, sid)
    return render_json()


def friends(request):
    my_friends = Friend.friends(request.user.id)
    friend_info = {frd.to_dict() for frd in my_friends}
    return render_json({'friends': friend_info})
