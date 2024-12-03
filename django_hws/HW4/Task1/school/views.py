from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    students_data = Student.objects.order_by(ordering).prefetch_related('teachers')
    context = {
        'object_list': students_data
    }

    return render(request, template, context)


def add_teachers(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()

    for student in students:
        for teacher in teachers:
            student.teachers.add(teacher)