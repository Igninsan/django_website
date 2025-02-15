from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

# Список товаров
def cart_list(request):
    if request.method == 'GET':
        query = models.CartModel.objects.all()
        context_object_name = {
            'cart_lst': query,
        }
        return render(request, template_name='cart/cart_list.html', context=context_object_name)


# Добавление товаров
def create_cart(request):
    if request.method == 'POST':
        form = forms.CartForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cart_lst')
    else:
        form = forms.CartForm()
    return render(request, template_name='cart/create_cart.html', context= {'form': form})


# Удаление товара
def delete_cart_view(request, id):
    cart_id = get_object_or_404(models.CartModel, id=id)
    cart_id.delete()
    return redirect('cart_lst')


# Редактирование товара
def update_cart_view(request, id):
    cart_id = get_object_or_404(models.CartModel, id=id)
    if request.method == 'POST':
        form = forms.CartForm(request.POST, instance=cart_id)
        if form.is_valid():
            form.save()
            return redirect('cart_lst')
    else:
        form = forms.CartForm(instance=cart_id)
    return render(request, template_name='cart/cart_update.html',
                  context={
                      'form': form,
                      'cart_id': cart_id
                  })