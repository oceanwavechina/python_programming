from django.db import models
from datetime import datetime

class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=100, default=1)

    # 参见 django文档 Meta options
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name='Category', on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.tutorial_series

# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published", default=datetime.now())

    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)


    def __str__(self):
        return self.tutorial_title

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers', null=True, blank=True)

    def __str__(self):
        return self.title


    # 删除数据库记录的同时删除磁盘上的文件
    def delete(self, *args, ** kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
