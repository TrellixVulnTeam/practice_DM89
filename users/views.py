from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm  # 导入了用户创建的表单


def logout_view(request):
    """注销用户视图函数，执行完后返回主页"""
    logout(request)  # 内置函数，直接注销用户
    # 返回主页
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """注册新的用户"""
    if request.method != 'POST':
        # 如果不是post方式请求，则创建一个新的用户表单。
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():  # 如果数据有效，包含非法字符，密码是否相同，恶意的事情
            # 调用表单中的方法save()，将用户名和密码以散列值保存到数据库中，并返回新创建的用户对象，将它储存到new_user中
            new_user = form.save()
            # 让用户自动登录，再重定向到主页,应该是都这么写的。
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)

