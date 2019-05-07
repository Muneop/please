"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from blog.views import blog_page, blog_api, enemyTest, EnemyAbility
from post_service.views import post_list
import post_service

'''
urlpatterns = [
    path('admin/', admin.site.urls),
]
'''

schema_view = get_swagger_view(title='Pastenbin API')

urlpatterns = [
    url(r'^rest-api/', include('rest_framework.urls')),
    url(r'^rest-swagger/', schema_view),
    url('admin/', admin.site.urls),


    #blog page
    url(r'^blog/', blog_page),

    # post_service page
    url(r'^post_service/', post_list),
    #rest
    url(r'^api/blog/', blog_api.as_view()),

    #test_db에서 데이터 가져오기
    #url(r'^blog/(?P<tag>\d+)', 'blog.views.EnemyAbility'),

]
