from django import forms  # forms表格的意思
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic  # 这里告诉django根据Topic模型创建表单。
        fields = ['text']  # field 领域  区域为text字段
        labels = {'text': ''}  # labels 标签 这里只是告诉django不要为字段生成标签。


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry  # 这里告诉django根据Entry模型创建表单。
        fields = ['text']  # 要填写的字段
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        # 通过django使用forms.Textarea函数，定制了字段text输入的小部件，将文本区域宽度设置为80，默认是40.cols表示列的意思

# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = Entry
#         fields = ['text']
#         labels = {'text': ''}
#         widgets = {'text': forms.Textarea(attrs={'cols': 80})}