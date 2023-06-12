from django.shortcuts import render
# 导入HttpResponse模块
from django.http import HttpResponse

# Create your views here.

# 定义视图函数
def index(request):

    #准备上下文：定义在字典中（测试数据）
    context = {'title': '测试模板数据'}
    return render(request, 'Book/index.html', context)