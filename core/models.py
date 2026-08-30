from django.db import models


class Memo(models.Model):
    title = models.CharField(max_length=200, verbose_name="タイトル")
    content = models.TextField(verbose_name="本文")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")

    def __str__(self):
        return self.title  # 管理画面のリストでタイトルが表示されるようにする
