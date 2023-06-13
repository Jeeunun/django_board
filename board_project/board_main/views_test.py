from django.shortcuts import render
from django.http import JsonResponse

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
def test_post_form(request):
    return render(request, 'test/test_post_form.html')

def test_post_handle(request):
    name = request.POST['my_name']
    email = request.POST['my_email']
    password = request.POST['my_password']
    print(name, email, password)