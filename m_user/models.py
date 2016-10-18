#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
COLLEGES=(
    ('tongxin','通信工程学院'),
    ('dianzi','电子工程学院'),
    ('jisuanji','计算机学院'),
    ('jidian','机电工程学院'),
    ('wuguang','物理与光电工程学院'),
    ('jingguan','经济与管理学院'),
    ('shutong','数学与统计学院'),
    ('renwen','人文学院'),
    ('waiguoyu','外国语学院'),
    ('ruanjian','软件学院'),
    ('weidianzi','微电子学院'),
    ('shengke','生命科学技术学院'),
    ('kongjian','空间科学与技术学院'),
    ('cailiao','先进材料与纳米科技学院'),
    ('wangan','网络与信息安全学院'),
)

class Muser(models.Model):
    user = models.OneToOneField(User)
    u_id = models.CharField(max_length=100,blank=True,default='')
    birthday = models.DateField(blank=True,default=None)
    university = models.CharField(max_length=50,blank=True,default='西安电子科技大学')
    college=models.CharField(max_length=50,choices=COLLEGES,blank=True,default=None)
    major=models.CharField(max_length=50,blank=True,null=True)
    introduction=models.TextField(blank=True,null=True)
    #img = models.ImageField(upload_to = 'media/', default = 'media/default/no-img.jpg')
    def __unicode__(self):
        if self.u_id:
            return smart_unicode(self.u_id)
        else:
            return smart_unicode(user)