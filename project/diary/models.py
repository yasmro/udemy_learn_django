from django.db import models
from django.utils import timezone
#DjangoではDatetune,nowのかわりにtimezone.nowでデータ取得

class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)

    # 管理画面のタイトル変更
    def __str__(self):
        return self.title
    
