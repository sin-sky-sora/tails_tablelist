from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from pprint import pprint
from uuid import uuid4
from random import randint,choices
import string

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

def random_colors() -> int:
    r,g,b = randint(0,255),randint(0,255),randint(0,255)
    return "#%02X%02X%02X" % (r,g,b)
def random_name(n:int) -> str:
    return "".join(choices(string.ascii_letters+string.digits,k=n))

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
        user_hash = uuid4()
        data["hash"] = str(user_hash)
        data["color"] = random_colors()
        data["name"] = random_name(12)
    return JsonResponse(data)