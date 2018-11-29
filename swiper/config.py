'''
第三方配置
'''

# 互亿无限短信配置
HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': 'C42331298',
    'password': '2d2284b74dc4972da3df3915fb17b28f',
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    'mobile': None,
    'format': 'json'
}

# qiniu config
QN_ACCESS_KEY = 'u9g03Jgymv7Bvqfo0alARfGdvcDXizfZmRIVbU7Z'
QN_SECRET_KEY = 'Sy7Ilv4k9PewOtgQTZzRij9m6h3NSdGs3VoVZRhN'
QN_BUCKET_NAME = 'swiper'
QN_BASE_URL = ''