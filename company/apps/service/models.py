from django.db import models
from apps.main.mixin import TimeBasedStampModel
from tinymce.models import HTMLField


ICON_CHOICES = (
        ("1", "TEST"),
        ("2", "TEST"),
        ("3", "TEST"),
        ("4", "TEST"),
        ("5", "TEST"),
        ("6", "TEST"),
        ("7", "TEST")
    )

class Services(TimeBasedStampModel):
  title = models.CharField(("Title"), max_length=50)
  short_content = models.CharField(("Short Content"), max_length=127)
  content = HTMLField(("Content"))
  icon = models.CharField(("Icon"),choices=ICON_CHOICES, max_length=150)

  class Meta:
    verbose_name = "Service"
    verbose_name_plural = "Services"

  def __str__(self) -> str:
      return self.title

