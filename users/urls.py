from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # 这是登录页面
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    # 这是注销页面
    url(r'^logout/$', views.logout_view, name='logout'),  # 导入的是本目录的views
    # 这是注册页面
    url(r'^register/$', views.register, name='register'),  # 导入的是本目录的views。包含users/register
]
