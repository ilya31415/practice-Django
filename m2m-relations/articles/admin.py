from django.contrib import admin

from .models import Article, Tag, ArticleTags


class ArticleInline(admin.TabularInline):
    model = ArticleTags
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass

