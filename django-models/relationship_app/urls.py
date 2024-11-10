# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView, LogoutView, LoginView
from .views import register
from .import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('login/<int:pk>/', LoginView.as_view(template_name='login'), name='login'),
    path('logout/<int:pk>/', LogoutView.as_view(template_name='logout'), name='logout'),
    path('register/', register, name='views.register'),
    path('books/', list_books, name='list_books'),  
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'), 
]