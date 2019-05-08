from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)  # 最大输入的字符串
    date_added = models.DateTimeField(auto_now_add=True)  # 自动生成当前日期
    # 用user模型建立一个外键关系模块owner，foreign外建的意思。
    owner = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = '主题'

    def __str__(self):
        """在界面上返回一个简介字符串表示"""
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic)  # foreign外来的意思，起一个继承的意思
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '信息'  # 显示的主题更改为entries

    def __str__(self):
        """返回数据模型的字符串"""
        return self.text[:50] + '...'
