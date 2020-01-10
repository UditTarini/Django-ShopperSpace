from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index")
def index2(request):
    return HttpResponse("Index2")    