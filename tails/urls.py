from django.urls import path,include
from .views import index,home,trade,trande_post,trade_details,trade_search,setting,welcome,chat,strategy
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
]