from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status = 'p')

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="ادرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="وضعیت")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ["position"]

    def __str__(self):
        return self.title

class Article(models.Model):
    STATU_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="ادرس مقاله")
    description = models.TextField(verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر مقاله")
    publish = models.DateTimeField(default=timezone.now(), verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATU_CHOICES, verbose_name="وضعیت")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name="article")
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ["-publish"]

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار(جلالی)"

    def __str__(self):
        return self.title

    def category_published(self):
        return self.category.filter(status=True)

    objects = ArticleManager()
