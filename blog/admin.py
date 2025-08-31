from django.contrib import admin
from blog.models import Post,Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title','author', 'status', 'id', 'created_date', 'updated_date')
    search_fields = ('title', 'author')
    list_filter = ('status', 'published_date')

