from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template_name = 'thelab/index.html'
    return render(request, template_name)


def calendar_view(request):
    template_name = 'thelab/onecolumn.html'
    return render(request, template_name)
