from . import models
from django.views import generic

# Список всей одежды
class AllClothesView(generic.ListView):
    template_name = 'clothes/all_clothes.html'
    context_object_name = 'all_clothes'
    model = models.Clothes

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

# def all_clothes(request):
#     if request.method == 'GET':
#         query = models.Clothes.objects.all().order_by('-id')
#         context_object_name = {
#             'all_clothes': query,
#         }
#         return render(request, template_name='clothes/all_clothes.html',
#                       context=context_object_name)


#детская одежда
class ChildrenClothesView(generic.ListView):
    template_name = 'clothes/children.html'
    context_object_name = 'children'
    model = models.Clothes

    def get_queryset(self):
        return self.model.objects.filter(tags__name='детская').order_by('-id')

# def children_clothes(request):
#     if request.method == 'GET':
#         query = models.Clothes.objects.filter(tags__name='детская').order_by('-id')
#         context_object_name = {
#             'children': query,
#         }
#         return render(request, template_name='clothes/children.html',
#                       context=context_object_name)


#подростковая одежда
class TeenageClothesView(generic.ListView):
    template_name = 'clothes/teenage.html'
    context_object_name = 'teenage'
    model = models.Clothes

    def get_queryset(self):
        return self.model.objects.filter(tags__name='подростковая').order_by('-id')

# def teenage_clothes(request):
#     if request.method == 'GET':
#         query = models.Clothes.objects.filter(tags__name='подростковая').order_by('-id')
#         context_object_name = {
#             'teenage': query,
#         }
#         return render(request, template_name='clothes/teenage.html',
#                       context=context_object_name)


#взрослая одежда (для взрослых)
class AdultClothesView(generic.ListView):
    template_name = 'clothes/adult.html'
    context_object_name = 'adult'
    model = models.Clothes

    def get_queryset(self):
        return self.model.objects.filter(tags__name='взрослая').order_by('-id')

# def adult_clothes(request):
#     if request.method == 'GET':
#         query = models.Clothes.objects.filter(tags__name='взрослая').order_by('-id')
#         context_object_name = {
#             'adult': query,
#         }
#         return render(request, template_name='clothes/adult.html',
#                       context=context_object_name)