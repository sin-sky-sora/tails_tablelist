from django.urls import path,include
from .views import *
urlpatterns = [
    path('',index,name="top"),
    path('welcome',welcome,name="welcome"),
    path('home',home,name="top_home"),
    path('trade',trade,name="trade"),
    path('post',trande_post,name="post"),
    path('trade/details/<int:pk>/',trade_details,name="trade_details"),
    path('search',trade_search,name="search"),
    path('chat',chat,name="chat"),
    path('strategy',strategy,name="strategy"),
    path('setting',setting,name="setting"),
    path('api/<str:cases>/',api,name="api"),
]