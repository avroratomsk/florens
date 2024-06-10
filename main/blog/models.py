from django.db import models
from django.urls import reverse

class BlogSettings(models.Model):
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  image = models.ImageField(upload_to="blog", blank=True, null=True, verbose_name="Изображение баннера")
  text = models.TextField(null=True, blank=True, verbose_name="Текст на странице")

class BlogCategory(models.Model):
  name = models.CharField(max_length=250, null=True, blank=True, db_index=True, verbose_name="Название статьи")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
  date_creation = models.DateField(auto_now_add=True)
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  image = models.ImageField(upload_to="blog-category", blank=True, null=True, verbose_name="Изображение статьи")

class Post(models.Model):
  name = models.CharField(max_length=250, null=True, blank=True, db_index=True, verbose_name="Название статьи")
  slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
  text = models.TextField(null=True, blank=True, verbose_name="Содержимое статьи")
  category = models.ManyToManyField(BlogCategory, null=True, blank=True, verbose_name='Категории')
  date_creation = models.DateField(auto_now_add=True)
  date_update = models.DateField(auto_now=True)
  image = models.ImageField(upload_to="blog", blank=True, null=True, verbose_name="Изображение статьи")
  meta_h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name="Заголовок первого уровня")
  meta_title = models.CharField(max_length=350, null=True, blank=True, verbose_name="Мета заголовок")
  meta_description = models.TextField(null=True, blank=True, verbose_name="Meta описание")
  meta_keywords = models.TextField(null=True, blank=True, verbose_name="Meta keywords")
  status = models.BooleanField(default=True, verbose_name="Статус публикации")

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("post", kwargs={"slug": self.slug})
  