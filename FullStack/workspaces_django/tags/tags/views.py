from django.shortcuts import render

def index(request):
    # {'name' : '채원'} -> 딕셔너리로 전달
    return render(request,'index.html',{'name':'채원'})
    # templates/index.html
