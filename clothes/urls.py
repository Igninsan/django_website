from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.AllClothesView.as_view(), name='all_clothes'),
    path('children/', views.ChildrenClothesView.as_view(), name='children_clothes'),
    path('teenage/', views.TeenageClothesView.as_view(), name='teenage_clothes'),
    path('adult/', views.AdultClothesView.as_view(), name='adult_clothes')
]