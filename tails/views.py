from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from pprint import pprint

def index(request):
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded:
        print("forwarded is true")
        print(forwarded.split(","))
    else:
        print("forwarded is false")
        print(request.META.get("REMOTE_ADDR"))
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
    return render(request,"search.html")
    
def setting(request):
    return HttpResponse("SETTING NOW")

def welcome(request):
    return render(request,"welcome.html")
    
def chat(request):
    return HttpResponse("chat")
    
def strategy(request):
    return HttpResponse("strategy")
    
def api(request,cases):
    data = {"type":"failed"}
    if cases == "user":
        """
            status:
                yet
                    ユーザー登録する必要がある
                already
                    ユーザーは既に登録されている
        """
        data["type"] = "success"
        data["status"] = "yet"
    return JsonResponse(data)