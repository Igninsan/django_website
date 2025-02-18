from django.shortcuts import get_object_or_404
from . import models, forms
from django.views import generic


# Список товаров
class CartListView(generic.ListView):
    template_name = 'cart/cart_list.html'
    context_object_name = 'cart_lst'
    model = models.CartModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


# def cart_list(request):
#     if request.method == 'GET':
#         query = models.CartModel.objects.all()
#         context_object_name = {
#             'cart_lst': query,
#         }
#         return render(request, template_name='cart/cart_list.html', context=context_object_name)


# Добавление товаров
class CreateCartView(generic.CreateView):
    template_name = 'cart/create_cart.html'
    form_class = forms.CartForm
    success_url = '/cart_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCartView, self).form_valid(form=form)

# def create_cart(request):
#     if request.method == 'POST':
#         form = forms.CartForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('cart_lst')
#     else:
#         form = forms.CartForm()
#     return render(request, template_name='cart/create_cart.html', context= {'form': form})


# Удаление товара
class DeleteCartView(generic.DeleteView):
    template_name = 'cart/confirm_delete.html'
    success_url = '/cart_list/'

    def get_object(self, *args, **kwargs):
        cart_id = self.kwargs.get('id')
        return get_object_or_404(models.CartModel, id=cart_id)


# def delete_cart_view(request, id):
#     cart_id = get_object_or_404(models.CartModel, id=id)
#     cart_id.delete()
#     return redirect('cart_lst')


# Редактирование товара
class UpdateCartView(generic.UpdateView):
    template_name = 'cart/cart_update.html'
    form_class = forms.CartForm
    success_url = '/cart_list/'

    def get_object(self, *args, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.CartModel, id=todo_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateCartView, self).form_valid(form=form)

# def update_cart_view(request, id):
#     cart_id = get_object_or_404(models.CartModel, id=id)
#     if request.method == 'POST':
#         form = forms.CartForm(request.POST, instance=cart_id)
#         if form.is_valid():
#             form.save()
#             return redirect('cart_lst')
#     else:
#         form = forms.CartForm(instance=cart_id)
#     return render(request, template_name='cart/cart_update.html',
#                   context={
#                       'form': form,
#                       'cart_id': cart_id
#                   })