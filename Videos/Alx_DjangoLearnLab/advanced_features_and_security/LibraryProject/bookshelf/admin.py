from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication_year in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add search capability for title and author
    search_fields = ('title', 'author')

    # Add filter for publication_year
    list_filter = ('publication_year',)

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
        )
    add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {'fiels': ('date_of_birth', 'profile_photo')})
        )
    

# Register the Book model with the custom admin configuration
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)