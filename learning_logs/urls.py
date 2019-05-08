"""这里要定义一个learing_logs的url模式"""
# from django.urls import path, include
from django.conf.urls import url
from . import views  # 导入当前文件夹的views文件 也就是learing_logs

# app_name = 'learning_logs'  # 这里还无法理解，2.0的版本需要写上这个才可以定义 learning_logs中url.py的namespace=
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),  # 路径为空格是为了链接到index.html显示主页。name=将这个url命名为具体的名称，让它在其他地方也可以引用
    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),  # 8000/topics路径链接到topice.html文件
    # # 这里是特定主页的详细界面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # # 用于添加新主题的网页。
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面，运用主题的id
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 这里需要传递编辑的条目页面的id
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
