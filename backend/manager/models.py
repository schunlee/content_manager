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
    group = ForeignKey(BusinessGroup, on_delete=models.CASCADE, verbose_name="分组", related_name='customers')  # 分组


class ClerkType(models.Model):
    '''
    客服类型
    通过django admin配置

    zalo, line, fb-messenger, whatsapp, lulu-zalo, lulu-fb-messenger, lulu-line, lulu-whatsapp, 外部链接
    '''
    name = CharField(max_length=50, blank=False, null=False, verbose_name="客服类型")

    class Meta:
        ordering = ('name',)


class Clerk(models.Model):
    '''
    客服
    '''
    clerk_number = CharField(max_length=50, blank=False, null=False, verbose_name="客服号码")
    note = TextField(blank=False, null=False, verbose_name="备注")
    clerk_type = ForeignKey(ClerkType, on_delete=models.CASCADE, verbose_name="类型", related_name="clerks")


class Country(models.Model):
    '''
    国家
    通过django admin配置
    '''
    name = CharField(max_length=100, null=False, blank=False, verbose_name="国家名称")


class App(models.Model):
    '''
    App
    '''
    BEHAVIOR_IN_APP_CHOICES = [
        ("inner", "内跳"),
        ("outer", "外跳")
    ]
    STATUS_IN_APP_CHOICES = [
        ("test", "待测试"),
        ("stop", "已停用"),
        ("develop", "开发中"),
        ("review", "提审中"),
        ("live", "在线")
    ]
    name = CharField(max_length=50, verbose_name="应用名称")
    behavior = CharField(max_length=10, choices=BEHAVIOR_IN_APP_CHOICES, default="outer", verbose_name="跳页方式")
    note = TextField(null=True, blank=True, verbose_name="备注")
    target_country = ForeignKey(Country, on_delete=True, verbose_name="主推国家")
    status = CharField(max_length=50, choices=STATUS_IN_APP_CHOICES, verbose_name="状态")
