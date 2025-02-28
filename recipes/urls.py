from django.urls import path
from . import views

urlpatterns= [
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_lst'),
    path('create_recipe/', views.CreateRecipeView.as_view(), name='create_recipe'),
    path('recipe_list/<int:id>/delete/', views.DeleteRecipeView.as_view(), name='delete_recipe'),
    path('recipe_list/<int:id>/ingredient_list/', views.IngredientListView.as_view(), name='ingredient_lst'),
    path('create_ingredient/', views.CreateIngredientView.as_view(), name='create_ingredient'),
]