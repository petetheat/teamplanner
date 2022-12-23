from django.shortcuts import render
from django.http import HttpResponse
import calendar

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
    mycalendar = Calendar(year, month)
    year_next, month_next = calendar._nextmonth(year, month)
    year_prev, month_prev = calendar._prevmonth(year, month)

    context_dict = {'year': year,
                    'month': month,
                    'year_next': year_next, 'month_next': month_next,
                    'year_prev': year_prev, 'month_prev': month_prev,
                    'calendar': mycalendar.formatmonth()}

    return render(request, template_name, context_dict)
