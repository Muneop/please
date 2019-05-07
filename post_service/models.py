from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    #게시물의 고유한 인덱스는 models.Model에 기본으로 포함되는 pk를 이용합니다.
    #2. 게시물의 제목, 1024자
    title = models.CharField(max_length=1024)
    #3. 게시물의 내용, 4096자
    body = models.CharField(max_length=4096)
    #4. 게시물의 작성자는 Django의 기본 User를 활용해 봅시다.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #5. 게시물의 작성시간, 자동으로 게시물이 등록되는 시간이 설정 되도록 합시다.
    regdate = models.DateTimeField(auto_created=True, auto_now_add=True)
    # 게시물의 고유 비밀번호는 author의 권한 인증을 따라갑시다.
# Create your models here.
