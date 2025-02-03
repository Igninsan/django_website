from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('в нашей библиотеке очень много книг!')

def text_and_photo(request):
    if request.method == 'GET':
        return HttpResponse('наша библиотека: <img src="https://sxodim.com/uploads/posts/2022/12/23/optimized/5f9e571b67068bd46df66207d78522d7_1400x790-q-85.jpg" />')

def system_time(request):
    if request.method == 'GET':
        return HttpResponse(f'{datetime.now()}')