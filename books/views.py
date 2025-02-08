from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models


#books list
def book_list_view(request):
    if request.method == 'GET':
        query = models.BookModel.objects.all().order_by('-id')
        context_object_name = {
            'book': query,
        }
        return render(request, template_name='book.html', context=context_object_name)

#books detail
def book_detail_view(request, id):
    if request.method == 'GET':
        query = get_object_or_404(models.BookModel, id=id)
        context_object_name = {
            'book_id': query,
        }
        return render(request, template_name='book_detail.html', context=context_object_name)


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('в нашей библиотеке очень много книг!')

def text_and_photo(request):
    if request.method == 'GET':
        return HttpResponse('наша библиотека: <img src="https://sxodim.com/uploads/posts/2022/12/23/optimized/5f9e571b67068bd46df66207d78522d7_1400x790-q-85.jpg" />')

def system_time(request):
    if request.method == 'GET':
        return HttpResponse(f'{datetime.now()}')