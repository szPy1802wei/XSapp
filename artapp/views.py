# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from artapp.models import ArtTag, Art


# Create your views here.
# get参数分为查询参数,表单参数
# jepg带alpha透明度的,png不带alpha


def index(request):
    # # 请求路径和请求方法
    # print(request.path, request.method)
    # # 请求头的源信息和GET请求参数(查询参数)
    # # print(request.META, request.GET)
    # print(request.GET.get('page'), request.GET.get('tag'))
    # # post请求参数(表单参数)
    # print(request.POST)
    # # return HttpResponse('<h1>你好</h1>')
    # # return JsonResponse({'name':'wei'})
    return render(request, 'art/list.html', context={'arts': Art.objects.all(),
                                                     'tags': ArtTag.objects.all()})


def edit_tags(request):
    # 添加标签类型的处理函数
    if request.method == 'GET':
        # 新增,修改
        # 判断是否为修改
        id = request.GET.get('id')
        if id:
            # 存在id即为修改
            tag = ArtTag.objects.get(id=id)
            return render(request, 'art/edit_tags.html', {'tag': tag})
        return render(request, 'art/edit_tags.html')
    else:
        # POST请求
        if request.POST.get('id'):
            tag = ArtTag.objects.get(id=request.POST.get('id'))
            tag.name = request.POST.get('title')
            tag.save()
        # 新增,修改
        else:
            tag = ArtTag()
            tag.name = request.POST.get('title')
            tag.save()
        return redirect('/artapp/list_tags/')   # 重定向,响应过来后又发一个新的请求


def delete_tag(request):
    id = request.GET.get('id')
    if id:
        result = ArtTag.objects.filter(id=id)
        if result.exists():
            result.delete()
    return redirect('/artapp/list_tags/')


def list_tags(request):
    return render(request, 'art/tags_list.html',
                  context={
                      'tags': ArtTag.objects.all()
                  })


# 展示文章详情页
def show_detail(request):
    # if request.method == 'GET':
    #     art_id = request.GET.get(id)
    #     if art_id:
    #         art = Art.objects.get(id=art_id)
    #         return render(request, 'art/detail.html', {'art': art})
    #     else:
    #         return render(request, 'art/tag_list.html')
    return render(request, 'art/detail.html')