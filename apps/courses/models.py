# _*_encoding:utf-8_*_
from __future__ import unicode_literals
from datetime import datetime

from DjangoUeditor.models import UEditorField

from django.db import models
from organization.models import CourseOrg, Teacher


# Create your models here.

class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name=u'课程机构', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u'课程名')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    detail = UEditorField(verbose_name=u'课程详情	', width=600, height=300, imagePath="course/ueditor",
                          filePath="course/ueditor", default='')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否轮播')
    degree = models.CharField(choices=(("cj", u"初级"), ("zj", u"中级"), ("gj", u"高级")), max_length=2, verbose_name=u'难度')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长（分钟数）')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=u'讲师', null=True, blank=True)
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u'封面图')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    category = models.CharField(default=u"后端开发", max_length=20, verbose_name=u'课程类别')
    tag = models.CharField(default="", max_length=10, verbose_name=u'课程标签')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    youneed_know = models.CharField(default="", max_length=300, verbose_name=u'课程需知')
    teacher_told = models.CharField(default="", max_length=300, verbose_name=u'老师告诉你')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_zj_nums(self):
        return self.lesson_set.all().count()

    get_zj_nums.short_description = "章节数"

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        return self.lesson_set.all()


class BannerCourse(Course):
    class Meta:
        verbose_name = '轮播课程'
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_lesson_video(self):
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长（分钟数）')
    url = models.CharField(max_length=200, verbose_name=u'访问地址', default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'名称')
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u'资源文件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name