from django.urls import path

from school.views import students_list, add_teachers

urlpatterns = [
    path('', students_list, name='students'),
    path('add_teachers', add_teachers, name='add')
]
