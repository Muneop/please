from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Post_blog, Ability
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView
import json

def blog_page(request):
    post_list_blog = Post_blog.objects.all()
    return HttpResponse('드디어 되고 있습니다! 옴뇬묘!!!!'+post_list_blog[0].title + post_list_blog[0].content)

def enemyTest(request):#테스트
    data = json.loads(request.raw_post_data)
    print(data)
    name = data['name']
    print(name)
    return HttpResponse('h')

def EnemyAbility(request, tag = None):
    entries = Ability.objects.get(tag = int(tag))
    data = entries.dic()
    return HttpResponse(json.dumps(data), content_type="application/json" )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_blog
        fields = '__all__'#버전이 바껴서 이부분을 추가해야됨.

class blog_api(GenericAPIView,mixins.ListModelMixin):
    queryset = Post_blog.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


#git 테스트를 위해서 적어봅니다.

#https://github.com/Muneop/please.git

#에에에에에에에에에에에오오오오오

