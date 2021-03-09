from django.urls import path,include
from .views import index,home,trade,trande_post,trade_details,trade_search,setting
urlpatterns = [
    path('',index,name="top"),
    path('home/',home,name="top_home"),
    path('trade/',trade,name="trade_home"),
    path('trade/post/',trande_post,name="trade_post"),
    path('trade/details/<int:pk>/',trade_details,name="trade_details"),
    path('trade/search/',trade_search,name="trade_search"),
    path('setting/',setting,name="setting"),
]