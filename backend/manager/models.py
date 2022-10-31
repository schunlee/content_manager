import uuid

from django.db import models

# Create your models here.
from django.db.models import CharField, TextField, PositiveIntegerField, TimeField, UUIDField, BooleanField, ForeignKey


class Article(models.Model):
    '''
    文章
    '''
    STATUS_IN_APP_CHOICES = [
        ("display", "显示"),
        ("hidden", "未显示")
    ]

    hash_id = UUIDField(default=uuid.uuid4, editable=False, verbose_name="Hashcode")
    title = CharField(max_length=300, blank=False, null=False, verbose_name="标题")
    description = TextField(blank=True, null=True, verbose_name="简介")
    status = CharField(max_length=10, choices=STATUS_IN_APP_CHOICES, default="hidden", verbose_name="文章状态")
    order_num = PositiveIntegerField(default=1, verbose_name="排序")
    create_time = TimeField(auto_now_add=True, verbose_name="文章创建时间")
    modified_time = TimeField(auto_now=True, verbose_name="文章修改时间")
    tt0 = TextField(blank=True, null=True, verbose_name="TT0")
    tt1 = TextField(blank=True, null=True, verbose_name="TT1")
    tt2 = TextField(blank=True, null=True, verbose_name="TT2")
    tt3 = TextField(blank=True, null=True, verbose_name="TT3")
    greeting = TextField(blank=True, null=True, verbose_name="招呼语")

    class Meta:
        ordering = ('create_time',)


class BusinessGroup(models.Model):
    '''
    分组
    通过django admin配置
    '''
    name = CharField(max_length=50, blank=False, null=False, verbose_name="分组名")


class Customer(models.Model):
    '''
    商户
    '''
    STATUS_IN_CUSTOMER_CHOICES = [
        ("normal", "正常"),
        ("stop", "停止")
    ]
    name = CharField(max_length=50, blank=False, null=False, verbose_name="商户名")
    status = CharField(max_length=10, choices=STATUS_IN_CUSTOMER_CHOICES, default="normal", verbose_name="状态")
    single_flag = BooleanField(default=False, verbose_name="是否去重")
    create_time = TimeField(auto_now_add=True, verbose_name="商户新增时间")
    modified_time = TimeField(auto_now=True, verbose_name="商户信息修改时间")
    group = ForeignKey(to=BusinessGroup, on_delete=models.CASCADE, verbose_name="分组", related_name='groups')  # 分组


class ClerkType(models.Model):
    '''
    客服类型
    通过django admin配置
    '''
    name = CharField(max_length=50, blank=False, null=False, verbose_name="客服类型")


class Clerk(models.Model):
    '''
    客服
    '''
    name = CharField(max_length=50, blank=False, null=False, verbose_name="名称")
    note = TextField(blank=False, null=False, verbose_name="备注")
