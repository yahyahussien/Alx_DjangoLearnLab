from django.contrib import admin
from .models import Book

@admin.register(Book)
 # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for the admin interface
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality
    search_fields = ('title', 'author')
# Register your models here.