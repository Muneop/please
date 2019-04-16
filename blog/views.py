from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Post
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

def blog_page(request):
    post_list = Post.objects.all()

    return HttpResponse('드디어 되고 있습니다! 옴뇸뇸뇸뇸뇸뇬묘!!!!'+post_list[0].title+post_list[0].content)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'#버전이 바껴서 이부분을 추가해야됨.

class blog_api(GenericAPIView,mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    #git 테스트를 위해서 적어봅니다.

#https://github.com/Muneop/please.git