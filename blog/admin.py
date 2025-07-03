from django.contrib import admin
from blog.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title', 'status', 'id', 'created_date', 'updated_date')
    search_fields = ('title', 'content')
    list_filter = ('status', 'published_date')