from django.shortcuts import render, redirect
from .models import MyBoard,MyMember
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password,check_password


def index(request):
    myboard = MyBoard.objects.all().order_by('-id')
    paginator = Paginator(myboard, 10)
    page_num = request.GET.get('page','1')

    # 페이지에 맞는 모델 가져오기
    page_obj = paginator.get_page(page_num)

    # 관련 메소드
    print('-'*30)
    print('type :',type(page_obj))
    print('count :',page_obj.count)
    print('num_pages :',page_obj.paginator.num_pages)
    print('page_range :',page_obj.paginator.page_range)
    print('has_next() :',page_obj.has_next())
    print('has_previous :',page_obj.has_previous())
    try:
        print('next_page_number() :',page_obj.next_page_number())
        print('previous_page_number() :',page_obj.previous_page_number())
    except:
        pass
    print('start_index() :',page_obj.start_index())
    print('end_index() :',page_obj.end_index())
    print('-' * 30)

    return render(request, 'index.html', {'list': page_obj})


def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})


def insert(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    else:
        myname = request.POST['myname']
        mytitle = request.POST['mytitle']
        mycontent = request.POST['mycontent']

        result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

        if result:
            return redirect('index')
        else:
            return redirect('insertform')


def update(request, id):
    if request.method == 'GET':
        return render(request, 'update.html', {'dto': MyBoard.objects.get(id=id)})
    else:
        mytitle = request.POST['mytitle']
        mycontent = request.POST['mycontent']

        myboard = MyBoard.objects.filter(id=id)
        result_title = myboard.update(mytitle=mytitle)
        result_content = myboard.update(mycontent=mycontent)

        if result_title + result_content == 2:
            return redirect(f'/detail/{id}')
        else:
            return redirect(f'/updateform/{id}')


def delete(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()

    if result_delete[0]:
        return redirect('index')
    else:
        return redirect(f'/detail/{id}')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        myname = request.POST['myname']
        mypassword = request.POST['mypassword']
        myemail = request.POST['myemail']

        mymember = MyMember.objects.create(myname=myname, mypassword=make_password(mypassword), myemail=myemail)
        mymember.save()
        return redirect('/')

    return redirect('/')

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else :
        myname = request.POST['myname']
        mypassword = request.POST['mypassword']

        mymember = MyMember.objects.get(myname=myname)

        if check_password(mypassword, mymember.mypassword) :
            request.session['myname'] = mymember.myname
            return redirect('/')
        else :
            return redirect('/login')

def logout(request):
    del request.session['myname']
    return redirect('/')
