from django.urls import path
from . import views

urlpatterns = [
    path('ts_list/', views.TsListView.as_view(), name='ts_list'),
    path('ts_form/', views.TsFormView.as_view(), name='parser'),
    path('rezka_list/', views.RezkaListView.as_view(), name='rezka_list'),
]