from django.contrib import admin
from .models import Author, Book


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'authors__name']
    list_filter = ['publication_date']
    list_display = ['title', 'publication_date', 'price']
    ordering = ['title']
    fields = ['title', 'authors','description', 'publication_date','cover_image', 'price']


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
