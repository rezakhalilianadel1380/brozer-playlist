from django.shortcuts import render,HttpResponse

def my_view(request):
    return HttpResponse('hello world')
