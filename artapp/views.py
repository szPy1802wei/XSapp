from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
# get参数分为查询参数,表单参数
# jepg带alpha透明度的,png不带alpha


def index(request):
    # 请求路径和请求方法
    print(request.path, request.method)
    # 请求头的源信息和GET请求参数(查询参数)
    # print(request.META, request.GET)
    print(request.GET.get('page'), request.GET.get('tag'))
    # post请求参数(表单参数)
    print(request.POST)
    # return HttpResponse('<h1>你好</h1>')
    # return JsonResponse({'name':'wei'})
    return render(request, 'art/list.html', context={'name': 'wei', 'age': 20})