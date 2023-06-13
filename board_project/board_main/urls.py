

from django.urls import path
from . import views_test 

urlpatterns = [
    path('', views_test.test_html_multi_data),
    path('test_json', views_test.test_json_data),
    #url에 test_json로 들어가면 views_test파일의 test_json_data를 입력해라    
    path('parameter_data', views_test.test_html_parameter_data)
     #url에 parameter_data로 들어가면 views_test파일의 test_json_data를 입력해라         
]
