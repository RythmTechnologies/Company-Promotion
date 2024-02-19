from django.db import models
from apps.main.mixin import TimeBasedStampModel
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Category(TimeBasedStampModel):
  name = models.CharField(("Category Name"), max_length=50)
  slug = AutoSlugField(
        populate_from="name", editable=False, always_update=True, blank=True
    )


  def blog_count(self):
        return Blog.objects.filter(category=self).count()

  class Meta:
    verbose_name = "Category"
    verbose_name_plural = "Categories"

  def __str__(self) -> str:
    return self.name



class Label(TimeBasedStampModel):
  name = models.CharField(("Label Name"), max_length=50)

  class Meta:
    verbose_name = "Label"
    verbose_name_plural = "Labels"


  def __str__(self) -> str:
    return self.name


class Blog(TimeBasedStampModel):
  author = models.ForeignKey(User, verbose_name=("Blog Author"), on_delete=models.CASCADE)
  title = models.CharField(("Blog Title"), max_length=50)
  image = models.ImageField(("Blog Image"), upload_to="blog/",height_field=None, width_field=None, max_length=None)
  content = HTMLField(("Blog Content"))
  category = models.ForeignKey(Category, verbose_name=("Blog Category"), on_delete=models.CASCADE)
  label = models.ManyToManyField(Label, verbose_name=("Blog Label"))
  slug = AutoSlugField(
        populate_from="title", editable=False, always_update=True, blank=True
    )

  class Meta:
    verbose_name = "Blog"
    verbose_name_plural = "Blogs"

  def __str__(self) -> str:
    return self.title