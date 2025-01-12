from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication_year in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add search capability for title and author
    search_fields = ('title', 'author')

    # Add filter for publication_year
    list_filter = ('publication_year',)

# Register the Book model with the custom admin configuration
admin.site.register(Book, BookAdmin)
