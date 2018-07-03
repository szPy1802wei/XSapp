from django.db import models

# Create your models here.
# 索引可以提高查找速度,适用于sql优化


class ArtTag(models.Model):
    name = models.CharField(max_length=20, verbose_name='作品类别', unique=True, blank=True, db_index=True)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name='最后修改时间', auto_now=True)
    



