from django.urls import path

from articles.views import articles_list, add_tags

urlpatterns = [
    path('', articles_list, name='articles'),
    path('', add_tags, name='tags')
]
