from django.shortcuts import render
from blog.models import BlogPost
from django.http import HttpResponse
from django.template import loader,Context
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers



def archive(request):
    '''
    老的django实现
    '''
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({ 'posts':posts })
    return HttpResponse(t.render(c))

class BlogSerializer(serializers.Serializer):
    '''
    序列化器，用以显示列表
    '''
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=150)
    body = serializers.CharField()
    timestamp = serializers.DateTimeField()
        
@api_view(['GET','OPTIONS'])
def restarchive(ruquest):
    '''
    rest_framework实现
    '''
    posts = BlogPost.objects.all()
    serializer = BlogSerializer(instance=posts,many=True)
    return Response(serializer.data)
    