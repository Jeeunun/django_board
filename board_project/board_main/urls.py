

from django.urls import path
from . import views_test, views

urlpatterns = [
#     path('', views_test.test_html_multi_data),
#     path('test_json', views_test.test_json_data),
#     #url에 test_json로 들어가면 views_test파일의 test_json_data를 입력해라    
#     path('parameter_data', views_test.test_html_parameter_data),
#     #url에 parameter_data로 들어가면 views_test파일의 parameter_data를 입력해라 
#     path('parameter_data2/<int:my_id>', views_test.test_html_parameter_data2),
#     #url에 parameter_data2로 들어가면 views_test파일의 test_html_parameter_data2를 입력해라 
#     path('test_post_handle', views_test.test_post_handle),
#     path('test_select_one/<int:my_id>', views_test.test_select_one), 
#     path('test_select_all', views_test.test_select_all),    
#     path('test_select_multi', views_test.test_select_multi),
#     path('test_update', views_test.test_update),     
    path('', views.home), 
    path('authors/', views.author_list),   
    path('authors/new', views.author_new),
    path('authors/<int:my_id>', views.author_detail),
    path('authors/<int:my_id>/update', views.author_update),
    path('posts/', views.post_list),
    path('post/new', views.post_new),
    path('post/<int:my_id>', views.post_detail),
    path('post/<int:my_id>/update', views.post_update),
    
]

