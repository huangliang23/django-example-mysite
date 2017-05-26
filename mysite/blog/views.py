from django.shortcuts import render
from blog.models import BlogPost
from django.http import HttpResponse
from django.template import loader,Context


# Create your views here.
def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({ 'posts':posts })
    return HttpResponse(t.render(c))
    