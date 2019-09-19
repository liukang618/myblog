from django.shortcuts import render,HttpResponse
from blog import models
import datetime
# Create your views here. 一个函数对应一个视图
def index(req):
    return render(req,'index.html')
def text(request): #request 是返回的内容
    times = datetime.datetime.now()
    data = {
        'time' : times
    }
    return render(request,'test.html',data)
    # return HttpResponse("<h1>ok</h1>")
User_List = []
def userinfo(request):
    if request.method == "POST":
        u = request.POST.get("username",None)
        s = request.POST.get("sex",None)
        e = request.POST.get("email",None)
        models.User_List.objects.create(
            username = u,
            sex=s,
            email=e
        )
    User_List = models.User_List.objects.all()
    return render(request,'userinfo.html',{"User_List":User_List})