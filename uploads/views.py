from django.shortcuts import render

# Create your views here.
from .models import User


def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        img = request.FILES.get('img')
        introduce = request.FILES.get('introduce')
        # 获取request的信息，进行实例化，然后保存
        user = User(name=username, img=img, introduce=introduce)
        user.save()
        return render(request, 'uploads/detail.html', locals())

    return render(request, 'uploads/add.html', locals())


def detail(request):
    user_list = User.objects.all()
    return render(request, 'uploads/detail.html', locals())
