from django.urls import path,include
from .views import index,home,trade,trande_post
urlpatterns = [
    path('',index,name="top"),
    path('home/',home,name="top_home"),
    path('trade/',trade,name="trade_home"),
    path('trade/post/',trande_post,name="trade_post"),
]