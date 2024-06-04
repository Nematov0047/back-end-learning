from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.Books.as_view(), name='books'),
    path('books/<int:book_id>/', views.GetBook.as_view(), name='get_book')
]