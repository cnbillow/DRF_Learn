from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from comment import models
import json

# Create your views here.


def article_list(request):
    # query_set = models.Article.objects.all().values('id', 'title', 'type', 'school__name')
    # for i in query_set:
    #     # i['created_time'] = i['created_time'].strftime('%Y-%m-%d')
    #     data = json.dumps(list(query_set), ensure_ascii=False)
    #     return HttpResponse(data)

    query_set = models.Article.objects.all().values('id', 'title', 'type', 'school')
    for i in query_set:
        school_obj = models.School.objects.filter(id=i['school']).first()
        id = school_obj.id
        name = school_obj.name
        i['school'] = {'id': id, 'name': name}
        return JsonResponse(list(query_set), safe=False)
    """
    可以看出。针对查询对应的学校信息，使用了for循环。它是一个外键字段，那如果再查询一个外键字段呢？再来一个for循环？代码太冗长了！
    """