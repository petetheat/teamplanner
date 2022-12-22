from django.shortcuts import render
from django.http import HttpResponse

from .utils import Calendar
import datetime


def index(request):
    template_name = 'thelab/index.html'
    t_now = datetime.datetime.now()
    year = t_now.year
    month = t_now.month
    return render(request, template_name, {'year': year, 'month': month})


def calendar_view(request, year, month):
    template_name = 'thelab/onecolumn.html'
    mycalendar = Calendar()

    context_dict = {'year': year,
                    'month': month,
                    'calendar': mycalendar.formatmonth(year, month)}

    return render(request, template_name, context_dict)
