from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'helloworld/templates.html')

def form(request):
    myname = request.POST['myname']

    params = {
        'myname': myname if myname != '' else 'ゲスト',
    }

    return render(request, 'helloworld/templates2.html', params)
