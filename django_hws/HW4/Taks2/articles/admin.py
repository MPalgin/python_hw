from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        tag_number = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                tag_number += 1
        if tag_number < 1:
            raise ValidationError('Должен быть выбран основной Тэг/раздел')
        if tag_number > 1:
            raise ValidationError('Основной Тэг/раздел должен быть один')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 2


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
