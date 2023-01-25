from . import views
from django.urls import path, include

app_name = 'calender'
urlpatterns = [
    # path(r'index/', views.index, name='index'),
    path(r'', views.CalendarView.as_view(), name='calendar'),
    path(r'event/new/', views.event, name='event_new'),
    path(r'event/edit/(?P<event_id>\d+)/', views.event, name='event_edit'),
]
