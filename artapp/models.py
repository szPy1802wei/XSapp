from django.db import models

# Create your models here.
# 索引可以提高查找速度,适用于sql优化


# 标签模型
class ArtTag(models.Model):
    name = models.CharField(max_length=20, verbose_name='作品类别', unique=True, blank=True, db_index=True)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name='最后修改时间', auto_now=True)


# 小说文章的模型 名字,作者,发布时间,点击次数,来源
class Art(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=False, verbose_name='文章标题')
    # 作者(模型类,建立多对一关联关系)
    author = models.CharField(max_length=20, blank=True, verbose_name='作者')
    summary = models.TextField(verbose_name='概述')
    # img_url = models.CharField(max_length=100, verbose_name='图片地址')
    # 返回的是路径,需要在setting的materoot设置,且安装文件上传的pillow包
    img = models.ImageField(verbose_name='文章图片', upload_to='')
    counter = models.IntegerField(default=0, verbose_name='阅读次数')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    # 文章类型,多对一
    tag = models.ForeignKey(ArtTag, on_delete=models.SET_NULL, null=True)

# 文章小节模型
# class


