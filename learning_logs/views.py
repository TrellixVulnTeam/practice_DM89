from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# from .forms import TopicForm

def index(request):
    """这是学习笔记的主页"""
    return render(request, 'learning_logs/index.html')


# Create your views here.
@login_required
def topics(request):
    """显示所有主题的模块"""
    # topics = Topic.objects.order_by("date_added")  # order_by应该是一个排序命令，根据date_added排序
    # 用户登录后request有一个user属性，代码Topic.obj～～user)让django从数据库中获取ower属性为当前用户的Topic对象。
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    # 确认请求是属于当前的用用户。如果不是就引发404错误
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')  # 减号的意思就是降序排列。
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """添加一个新的主题"""
    if request.method != 'POST':
        # 如果没有提交数据：创建一个新的表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理。
        form = TopicForm(request.POST)
        if form.is_valid():  # 检查数据完整
            new_topic = form.save(commit=False)  # 将表单传给new_topic不保存到数据库中。
            new_topic.owner = request.user  # 设置新的主题属性设置为当前的用户
            new_topic.save()  # 然后在添加到数据库中
            # form.save()  # 添加数据到数据库
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):  # topic_id为形参，下面用于获取某一个主题
    """在特定的主题中添加新的条目"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 如果不是post请求，就建立一个新的清单（entryform实例化）
        form = EntryForm()
    else:
        # POST data submitted; process data,,post提交数据，对数据进行处理。
        form = EntryForm(data=request.POST)  # 通过post数据创建表单
        if form.is_valid():  # 检查数据是否有效
            new_entry = form.save(commit=False)  # 添加数据到表单中，不保存在数据库中，commit提交的意思
            new_entry.topic = topic  # 将new_entry的属性topic设置为从数据库中获得的主题。
            new_entry.save()  # 储存数据
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))  # 重定向到topic视图函数，列表args表示重定向到，新添加的主题。
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑已有的条目"""
    entry = Entry.objects.get(id=entry_id)  # 获取要修改的条目对象，以及相关联的主题，
    topic = entry.topic  #
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 如果是第一次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)  # instance实例的意思，
    else:
        # 以POST提交数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        # 传递实参instance=entry, data=request.POST让django根据，request.post中的数据进行修改。
        if form.is_valid():  # 检查是否有效，
            form.save()  # 储存在数据库中
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
