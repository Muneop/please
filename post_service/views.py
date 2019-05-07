from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http.response import HttpResponse
from post_service.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def post_list(request):
    #원래코드
    template = get_template('post_list.html')

    page_data = Paginator(Post.objects.all(), 5)
    page = request.GET.get('page')
    try:
        posts = page_data.page(page)
    except PageNotAnInteger:
        posts = page_data.page(1)
    except EmptyPage:
        posts = page_data.page(page_data.num_pages)

    context = Context({'post_list': posts, 'current_page': page, 'total_page': range(1, page_data.num_pages+1)})

    #원래코드시작
    #context = Context({'post_list' : Post.objects.all()})
    return HttpResponse(template.render(context.flatten()))
    #원래코드끝
    #장고가 업데이트 되면서 render(context)를 그대로 넘겨줄 수 가 없음.
    #flatten()을 사용하여 dict형식으로 바꿔줘야됨

