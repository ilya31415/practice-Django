from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTags


class ArticleInlineFormset(BaseInlineFormSet):
    def clean(self):

        real_forms = [form for form in self.forms if not form.cleaned_data.get('DELETE')]
        set_forms = set([form.cleaned_data.get('tag').id for form in real_forms])
        main_foms = [form.cleaned_data.get('is_main') for form in real_forms if
                     form.cleaned_data.get('is_main') == True]

        if len(set_forms) != len(real_forms):
            raise ValidationError('дублирование Тега')
        elif len(main_foms) > 1:
            raise ValidationError('дублирование главного Тега')

        return super().clean()


class ArticleInline(admin.TabularInline):
    model = ArticleTags
    extra = 0
    formset = ArticleInlineFormset


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
