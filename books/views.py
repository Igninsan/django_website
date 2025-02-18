from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models, forms
from django.views import generic

# Поиск
class SearchView(generic.ListView):
    template_name = 'book.html'

    def get_queryset(self):
        return models.BookModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


# create reviews
class CreateReviewView(generic.CreateView):
    template_name = 'create_review.html'
    form_class = forms.CreateReviewForm
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)


# def create_review(request):
#     if request.method == 'POST':
#         form = forms.CreateReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = forms.CreateReviewForm()
#     return render(request, template_name='create_review.html', context={'form': form})



#books list
class BookListView(generic.ListView):
    template_name = 'book.html'
    model = models.BookModel

    def get_queryset(self):
        return self.model.objects.all()

# def book_list_view(request):
#     if request.method == 'GET':
#         query = models.BookModel.objects.all().order_by('-id')
#         context_object_name = {
#             'book': query,
#         }
#         return render(request, template_name='book.html', context=context_object_name)

#books detail
class BooksDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, *args, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.BookModel, id=book_id)

# def book_detail_view(request, id):
#     if request.method == 'GET':
#         query = get_object_or_404(models.BookModel, id=id)
#         context_object_name = {
#             'book_id': query,
#         }
#         return render(request, template_name='book_detail.html', context=context_object_name)


class AboutMeView(generic.View):

    def get(self, request):
        return HttpResponse('в нашей библиотеке очень много книг!')


# def about_me(request):
#     if request.method == 'GET':
#         return HttpResponse('в нашей библиотеке очень много книг!')


class TextAndPhotoView(generic.View):

    def get(self, request):
        return HttpResponse('наша библиотека: <img src="https://sxodim.com/uploads/posts/2022/12/23/optimized/5f9e571b67068bd46df66207d78522d7_1400x790-q-85.jpg" />')


# def text_and_photo(request):
#     if request.method == 'GET':
#         return HttpResponse('наша библиотека: <img src="https://sxodim.com/uploads/posts/2022/12/23/optimized/5f9e571b67068bd46df66207d78522d7_1400x790-q-85.jpg" />')


class SystemTimeView(generic.View):

    def get(self, request):
        return HttpResponse(f'{datetime.now()}')


# def system_time(request):
#     if request.method == 'GET':
#         return HttpResponse(f'{datetime.now()}')