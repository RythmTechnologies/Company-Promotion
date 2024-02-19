from django.shortcuts import render,redirect
from apps.main.mixin import HttpRequest, HttpResponse
from .models import Blog, Category


# Main Blog View Start
def site_blog(request: HttpRequest) -> HttpResponse:

  context = {}
  blog = Blog.objects.all()
  context["blogs"] = blog

  return render(request, "pages/blog.html", context)
# Main Blog View End

# Single Blog View Start
def site_single_blog(request: HttpRequest, slug: str) -> HttpResponse:
  context = {}
  blog = Blog.objects.filter(slug=slug).first()
  posts = Blog.objects.all()
  category = Category.objects.all()

  context["posts"] = posts
  context["blog"] = blog
  context["categories"] = category

  return render(request, "pages/blog-details.html", context)

# Single Blog View End