from django.urls import path

from . import views

app_name = 'thelab'
urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/<int:year>/<int:month>/', views.calendar_view, name='calendar'),
]
