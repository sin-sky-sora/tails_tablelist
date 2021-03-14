from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
import ipinfo
from pprint import pprint

def index(request):
    pprint(vars(request))
    if request.ipinfo is None:
        print(request.ipinfo)
    else:
        pprint(vars(request.ipinfo))
    return redirect("top_home")
    
def home(request):
    return render(request,"home.html")

def trade(request):
    return render(request,"trade.html")

def trande_post(request):
    return render(request,"post.html")

def trade_details(request,pk):
    return render(request,"trade.details.html")

def trade_search(request):
    return render(request,"trade.search.html")
    
def setting(request):
    return HttpResponse("SETTING NOW")

def welcome(request):
    return HttpResponse("welcome")
def chat(request):
    return HttpResponse("chat")
def strategy(request):
    return HttpResponse("strategy")