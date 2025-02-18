from django.urls import path

from . import views

urlpatterns= [
    path('', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:id>/', views.BooksDetailView.as_view(), name='book_detail'),
    path('create_review/', views.CreateReviewView.as_view(), name='create_review'),


    path('about_me/', views.AboutMeView.as_view(), name='about_me'),
    path('text_and_photo', views.TextAndPhotoView.as_view(), name='text_and_photo'),
    path('system_time', views.SystemTimeView.as_view(), name='system_time'),
    path('search/', views.SearchView.as_view(), name='search'),
]