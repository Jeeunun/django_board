from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Test

# create your views here. 

# get요청시 html파일 그대로 return
def test_html(request):
    return render(request, 'test/test.html')

# get요청시 html+data return (단일데이터)
def test_html_data(request):
    my_name = "hongildong"
    return render(request, 'test/test.html', {'name': my_name})

# get요청시 html+multi data return (멀티데이터)
def test_html_multi_data(request):
    data = {
        'name': 'hongildong',
        'age': 20
    }
    return render(request, 'test/test.html', {'data': data})

# get요청시 data만 return (json데이터)
def test_json_data(request):
    data = {
        'name': 'hongildong',
        'age': 20
    }
    # render라는 의미는 웹개발에서 일반적으로 화면을 return해줄때 사용하는 용어이다. 
    # python의 dict와 유사한 json으로 변환해서 return
    return JsonResponse(data)

# 사용자가 get요청으로 쿼리파라미터 방식 데이터를 넣어올 때
# 사용자가 get요청으로 데이터를 넣어오는 방식 2가지
# 1) 쿼리파라미터 방식 : localhost:8000/author?id=10&name=hongildong 과 같은 방식

def test_html_parameter_data(request):
    id = request.GET.get('id')   
    name = request.GET.get('name')

    # print(id)
    # print(name)
    #사용자가 request요청 -> request head + request body made by 웹브라우저 
    #       -> urls.py -> views_test.py -> 화면
    # request를 get요청-> id와 name을 get 하겠다. 
    return render(request, 'test/test.html', {})

# 실습 : name, email, password 받아서 화면에 dict형태로
def test_html_parameter_data(request):
    name = request.GET.get('name')   
    email = request.GET.get('email')
    password = request.GET.get('password')  
    data = {
        'name': name ,
        'email': email,
        'password': password
    }
    return render(request, 'test/test.html', {"my_data": data})   

# 2) pathvariable 방식(좀 더 현대적인 방식): localhost:8000/author/10 과 같은 방식
def test_html_parameter_data2(request, my_id):
    print(my_id)
    return render(request, 'test/test.html', {})   

# form태그를 활용한 post방식
# 먼저 화면을 rendering해주는 method
# def test_post_form(request):
#     return render(request, 'test/test_post_form.html')

# test_post_handle url에 request가 post형식으로 들어오면 if 문 
# ->"http://localhost:8000/test_post_handle"에 request save.
# / post형식이 아니면(get요청) else문 
# -> test_post_form.html의 "http://localhost:8000/test_post_handle"(홈화면)로 이동
def test_post_handle(request):
    if request.method == 'POST':
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
        # DB에 insert -> save함수 사용.
        # DB의 테이블과 sync가 맞는 Test클래스에서 객체를 만들어 save
        t1 = Test()
        t1.name = my_name
        t1.email = my_email
        t1.password = my_password
        t1.save()
        return  redirect('/') #home으로 가라 => localhost:8000/
    else:
        return render(request, 'test/test_post_form.html')
    

def test_select_one(request, my_id):
    # 단 건 만을 조회할 때 get() 함수 사용.
    t1 = Test.objects.get(id=my_id)
    # test class의 object를 get()   
    return render(request, 'test/test_select_one.html', {'data' : t1})


def test_select_all(request):
    # 모든 data조회 시 select * from XXXX: all() 함수 사용
    tests = Test.objects.all
    # 타입을 호출하고 값을 찍어봐야한다. 
    # for a in tests:
    #     print(a.name) #dict가 아니라 객체이기 때문에 a['name']이 아니라 a.name으로 !
    #     print(a.email)
    #    print(a.password)
    #-> for 문의 실행 그대로 test/test_select_all.html 실행된다. 
    return render(request, 'test/test_select_all.html',{'datas':tests})
    # datas에 tests를 담아 test_select_all.html 화면에 response

# where조건으로 다건을 조회할 땐 filter()함수 사용.
def test_select_multi(request):
    my_name = request.GET.get('name')
    t2 = Test.objects.filter(name = my_name) 
    return render(request, 'test/test_select_multi.html', {'datas': t2})   
# request시 url "localhost:8000/test_select_multi" 에서 
# test_select_multi method의 데이터를 response 
# 데이터? => filter

# update를 하기 위해서는 해당 건을 사전에 조회하기 위한 id값이 필요하다.
# 메서드는 등록과 동일하게 save()함수 사용
def test_update(request):
    if request.method == 'POST':
        my_id = request.POST['my_id']
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
        print(type(my_id))
        # t1 = Test()
        # t1.name = my_name
        # t1.email = my_email
        # t1.password = my_password
        # t1.save()
        return  redirect('/') 
    else:
        return render(request, 'test/test_update.html')