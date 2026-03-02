from django.contrib import admin
from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published', 'created_at', 'published_at']
    list_filter = ['published', 'category', 'tags']
    list_editable = ['published']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Content', {'fields': ('title', 'slug', 'excerpt', 'content', 'cover_image')}),
        ('Taxonomy', {'fields': ('category', 'tags')}),
        ('Publishing', {'fields': ('published', 'published_at')}),
    )
