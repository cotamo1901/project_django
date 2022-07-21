from django.shortcuts import render

from core.erp.models import Category


def myfirstview(request):
    data = {
        'name': 'john',
        'categories': Category.objects.all()
    }
    return render(request, 'home.html', data)
