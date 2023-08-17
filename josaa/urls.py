from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='josaa-home'),
    path('start/', views.start,name='josaa-start'),
    path('start/rank/', views.rank_analyser,name='josaa-analyser'),
    path('start/analyser/', views.analyser,name='josaa-analyser2'),
    path('start/analyser/display1', views.display1,name='josaa-display1'),
    path('start/analyser2/', views.analyser2,name='josaa-analyser2'),
    path('start/analyser2/display2', views.display2,name='josaa-display2'),
    path('start/analyser3/', views.analyser3,name='josaa-analyser2'),
    path('start/analyser3/display3', views.display3,name='josaa-display2'),
    path('start/analyser4/', views.analyser4,name='josaa-analyser2'),
    path('start/analyser4/display4', views.display4,name='josaa-display2'),
    path('start/rank/display', views.display,name='josaa-display'),
]