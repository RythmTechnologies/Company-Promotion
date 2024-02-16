from django.db import models
from django.http import HttpResponse
import typing as t
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect

RedirectOrResponse = t.Union[HttpResponseRedirect, HttpResponse]

# TimeBasedStamp Model Start
class TimeBasedStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
# TimeBasedStamp Model End


# Seo
def robots_txt(request: HttpRequest) -> HttpResponse:
    lines = [
        "User-agent: *",
        "Disallow:",
        # "Sitemap: https://www.dytsedanurciray.com/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
# Seo End