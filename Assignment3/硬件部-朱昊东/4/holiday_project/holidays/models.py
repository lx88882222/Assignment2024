from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='holidays_user_set',  # 添加 related_name 参数
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='holidays_user_set',  # 添加 related_name 参数
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Date(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    holiday_info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dates = models.ManyToManyField(Date)

    def add_holiday(self, date, holiday_info):
        date.holiday_info = holiday_info
        date.save()
        self.dates.add(date)

    def remove_holiday(self, date):
        date.holiday_info = ""
        date.save()
        self.dates.remove(date)

    def get_date(self, year, month, day):
        return self.dates.filter(year=year, month=month, day=day).first()

    def __str__(self):
        return f"Calendar of {self.user.username}"