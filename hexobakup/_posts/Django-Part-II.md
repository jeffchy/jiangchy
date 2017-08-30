---
title: Django Part II
date: 2017-01-18 22:44:45
tags:
- Web
- python
- Django
categories:
- Tech
- Note
---
Let's give some detailed discussion on **View** **Model** and **Templates**
<!-- more -->
### Templates
* First, create a directory called templates in your appname directory. Django will look for templates in there.
* white the tamplate code in an .html file, eg: index.html
# An example in the official documentation
```html
{% extends "base_generic.html" %}

{% `block`title %}{{ section.title }}{% endblock %}

{% `block` content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}
```
# about the [grammar](https://docs.djangoproject.com/en/1.10/ref/templates/language/)?
* {{ variables }} 解释器会将这样的variable替换成其变量名代表的值,即一个context中key对应的value,或者是一个类的属性
* filters，用小竖线来表示“|”，如{{ name|lower }},lower是一个过滤器，将name过滤一遍，使得它全部变成小写，filter支持嵌套,这样可以不断的进行过滤
* 常用的filter:default length filesizeformat
* 主要有集中作用：控制流，也可以output text,还可以引入外部的文件，有的tag需要有begin和end
* [完整的`标签`的类型](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/#ref-templates-builtins-`标签`)
* templates的继承，可以通过继承将模板文件拆分成各种小块，具体标签：extends block,block的名字需要不同


# 如何load模板
* 在view中 import django.template.loader, 使用get_template(template_name, using=None)方法
* 使用select_template(template_name_list, using=None)
* 在view.py中，在load完tenplates之后，我们就可以同样通过数据模型（models),获取服务器端的数据，形成一个dict，也就是context。
* 使用render，Template.render(context=None, request=None),在这一步我们将最终的templates提交回当初的request，浏览器得到一个http请求，并且load模板，填充乃荣，最终发送一个httpresponse响应回馈给请求的过程就正式完成了。

### shortcuts
# render (example)
```python
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

```
# get_objects_or_404()
```python
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```
同样get_list_or_404()也是类似的
