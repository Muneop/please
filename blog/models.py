from django.db import models

'''
간단한 블로그 만들기
블로그는 다양한 post로 구분 됨.
하나의 포스팅에는 제목/내용/작성시간 등으로 구분됨.
즉 제목/내용/작성시간이 데이터의 기본
'''

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=2048)
    reg_date = models.DateTimeField(auto_created=True, auto_now=True)

class Blog(models.Model):
    Title = models.CharField('TITLE', max_length= 50)
    Content = models.TextField('CONTENT')

    def __str__(self):
        return self.Title
# Create your models here.
