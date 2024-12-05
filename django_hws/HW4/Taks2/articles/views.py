from django.shortcuts import render

from articles.models import Article, Tag


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = '-published_at'
    articles = Article.objects.all()
    context = {'object_list': articles}

    return render(request, template, context)


def add_tags(request):
    tag_list = ['Наука', 'Здоровье', 'Культура', 'Город', 'Космос', 'Международные отношения']

    for tag in tag_list:
        Tag.objects.create(name=tag)
