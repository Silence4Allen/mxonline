# _*_encoding:utf-8_*_
__author__ = 'Allen'
__date__ = '2018/11/25 10:43'
from django.conf.urls import url, include

from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView
from .views import MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),

    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),

    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail"),

    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

    # 我的课程
    url(r'^my_course/$', MyCourseView.as_view(), name="my_course"),

    # 我的收藏-课程机构
    url(r'^my_fav/org/$', MyFavOrgView.as_view(), name="my_fav_org"),

    # 我的收藏-授课讲师
    url(r'^my_fav/teacher/$', MyFavTeacherView.as_view(), name="my_fav_teacher"),

    # 我的收藏-公开课程
    url(r'^my_fav/course/$', MyFavCourseView.as_view(), name="my_fav_course"),

    # 我的消息
    url(r'^mymessage$', MyMessageView.as_view(), name="mymessage"),
]
