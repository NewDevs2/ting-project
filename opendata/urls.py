from django.urls import path
from . import views

from .views import Main, AptPrice

app_name = 'opendata'

urlpatterns = [
    path('', views.index, name='index'),  #
    path('', Main.as_view()),  #home 화면 정의
    path('aptprice/', AptPrice, name='aptprice'),
    path('stockprice/', views.StockIndex, name = 'stockindex'),
    ]

"""
    #profile 관련
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
    
    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    """