from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import redirect, render, get_object_or_404

def index(request):
    return redirect("home")
    
def home(request):
    return render(request,"home.html")

def trade(request):
    return render(request,"trade.html")

def trande_post(request):
    return render(request,"trade.post.html")