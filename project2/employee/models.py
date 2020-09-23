from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.CharField('部署名', max_length=30)
    created_at = models.DateTimeField('日付', default=timezone.now)

    # admin panelで部署名を返す
    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField('部活名', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField('名', max_length=20)
    last_name = models.CharField('姓', max_length=20)
    email = models.EmailField('メール', blank=True)
    # 第1引数に関連づけるモデル
    # 第2引数にForeign Keyの説明（項目名）
    # 第3引数on_delete=models.PROTECTは関連するデータを全削除しないと削除できない
    department = models.ForeignKey(
        Department, 
        verbose_name='部署', 
        on_delete=models.PROTECT,
    )
    # 複数ルックアップ項目＝ManyToManyField
    club = models.ManyToManyField(
        Club,
        verbose_name='部活'
    )
    created_at = models.DateTimeField('日付', default=timezone.now)
    # 既存modelに項目を追加するとき＝デフォルト値セット
    address = models.CharField('住所', max_length=20, blank=True)

    def __str__(self):
        return '{0} {1} {2}'.format(self.last_name, self.first_name, self.department)
    