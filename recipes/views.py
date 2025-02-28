from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views.generic import ListView, CreateView, DeleteView


class RecipeListView(ListView):
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipe_lst'
    model = models.RecipeModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class IngredientListView(ListView):
    template_name = 'recipes/ingredient_list.html'
    context_object_name = 'ingredient_lst'
    model = models.IngredientModel

    def get_queryset(self):
        recipe_id = self.kwargs.get('id')
        return self.model.objects.filter(recipe_id=recipe_id).order_by('-id')


class CreateRecipeView(CreateView):
    template_name = 'recipes/create_recipe.html'
    form_class = forms.RecipeForm
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateRecipeView, self).form_valid(form=form)


class CreateIngredientView(CreateView):
    template_name = 'recipes/create_ingredient.html'
    form_class = forms.IngredientForm
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateIngredientView, self).form_valid(form=form)


class DeleteRecipeView(DeleteView):
    template_name = 'recipes/confirm_delete.html'
    success_url = '/recipe_list/'

    def get_object(self, *args, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(models.RecipeModel, id=recipe_id)

