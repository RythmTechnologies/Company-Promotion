from django.db import models
from apps.main.mixin import TimeBasedStampModel
from django.core.validators import MaxValueValidator
from tinymce.models import HTMLField

class Testimimonials(TimeBasedStampModel):
  author = models.CharField(("Author"), max_length=150)
  title = models.CharField(("Title"), max_length=150)
  image = models.ImageField(("Image"), upload_to="testimoninials/", height_field=None, width_field=None, max_length=None)
  star = models.PositiveIntegerField(("Star Point"),default = 1, validators = [MaxValueValidator(5)])
  content = HTMLField(("Testimonial Content"), max_length = 400)

  class Meta:
    verbose_name = "Testimonial"
    verbose_name_plural = "Testimonials"

  def __str__(self) -> str:
      return self.author