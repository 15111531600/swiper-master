from lib.http import render_json

from social.logic import get_rcmd_user

# Create your views here.
def get_user(request):
    '''get user list'''
    group_num = int(request.GET.get('group_num',0))
    start = group_num * 5
    end = start + 5
    users = get_rcmd_user(request.user)[start:end]

    result = [user.to_dict() for user in users]
    return render_json(result)


def like(request):
    '''like'''
    return render_json()


def superlike(request):
    '''superlike'''
    return render_json()


def dislike(request):
    '''dislike'''
    return render_json()


def rewind(request):
    '''rewind'''
    return render_json()
