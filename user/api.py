from lib.http import render_json
from common import error
from user.logic import send_verify_code, check_vcode
from user.models import User
from user.forms import ProfileForm


def get_verify_code(request):
    '''手机注册'''
    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)
    return render_json(None, 0)


def login(request):
    '''短信验证登录'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if check_vcode(phonenum, vcode):
        # 获取用户
        user, created = User.objects.get_or_create(phonenum=phonenum)
        # 记录登录状态
        request.session['uid'] = user.id
        return render_json(user.to_dict())
    else:
        return render_json(None, error.VCODE_ERROR)


def get_profile(request):
    '''获取个人资料'''
    user = request.user
    return render_json(user.profile.to_dict())


def modify_profile(request):
    '''修改个人资料'''
    form = ProfileForm(request.POST)
    if form.is_valid():
        user = request.user
        user.profile.__dict__.update(form.cleaned_data)
        user.profile.save()
        return render_json(None)
    else:
        return render_json(form.errors, error.PROFILE_ERROR)


def upload_avatar(request):
    '''头像上传'''
    pass
