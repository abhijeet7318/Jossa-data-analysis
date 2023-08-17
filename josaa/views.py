from django.shortcuts import render
from .models import programm
from django.db.models import Q
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<h1>Hello</h1>')

from django.http import HttpResponse
from django.template import loader

def home(request):
#   template = loader.get_template('first.html')
  return render(request,'index.html')

def start(request):
  return render(request,'start.html')

def rank_analyser(request):
  return render(request,'rank-anlyser.html')

def analyser(request):
  return render(request,'analyser.html')

def analyser2(request):
  return render(request,'analyser2.html')

def analyser3(request):
  return render(request,'analyser3.html')

def analyser4(request):
  return render(request,'analyser4.html')

def display(request):
  rankk = float(request.POST.get("rank"))
  yearr = float(request.POST.get("year"))
  rounddd = float(request.POST.get("roundd"))
  cate = str(request.POST.get("category"))
  gend = str(request.POST.get("gender"))
  context={
    'ps': programm.objects.all().order_by('open'),
    'rank1': rankk,
    'cate1': cate,
    'gend1': gend,
    'year1': yearr,
    'roundd1':rounddd
  }
  
  return render(request,'display.html',context)

def display1(request):
  rankk2 = float(request.POST.get("rank2"))
  cate2 = str(request.POST.get("category2"))
  gend2 = str(request.POST.get("gender2"))
  branch22 = str(request.POST.get("branch2"))
  ps_filtered = programm.objects.filter(
    program__icontains=branch22.strip(),
    roundd=6,
    year=2022,
    seat_type=cate2,
    gender=gend2
  ).order_by('open')
 

  context={
    'ps': ps_filtered,
    'rank12': rankk2,
    'branch12':branch22
  }
  
  return render(request,'display1.html',context)

def display2(request):
  rankk3 = float(request.POST.get("rank3"))
  cate3 = str(request.POST.get("category3"))
  gend3 = str(request.POST.get("gender3"))
  iitt3 = str(request.POST.get("iit3"))
  ps_filtered = programm.objects.filter(
    roundd=6,
    year=2022
  ).order_by('open')

  context={
    'ps': ps_filtered,
    'rank13': rankk3,
    'cate13': cate3,
    'gend13': gend3,
    'iit13':iitt3
  }
  
  return render(request,'display2.html',context)

def display3(request):
  cate4 = str(request.POST.get("category4"))
  gend4 = str(request.POST.get("gender4"))
  iitt4 = str(request.POST.get("iit4"))
  ps_filtered = programm.objects.filter(
    roundd=6,
    gender=gend4,
    seat_type=cate4,
    institute=iitt4
  ).order_by('year')
  ps_filtered_2 = programm.objects.filter(
    roundd=6,
    gender=gend4,
    seat_type=cate4,
    institute=iitt4,
    year=2022
  ).order_by('year')
  context={
    'ps': ps_filtered,
    'ps2':ps_filtered_2
  }
  
  return render(request,'branch-trends.html',context)

def display4(request):
  cate5 = str(request.POST.get("category5"))
  gend5 = str(request.POST.get("gender5"))
  branch55 = str(request.POST.get("branch5"))
  ps_filtered = programm.objects.filter(
    program__icontains=branch55.strip(),
    roundd=6,
    gender=gend5,
    seat_type=cate5
  ).exclude(program__icontains='Dual Degree').order_by('year')


  ps_filtered_2 = programm.objects.filter(
    program__icontains=branch55.strip(),
    roundd=6,
    gender=gend5,
    seat_type=cate5,
    year=2021
  ).exclude(program__icontains='Dual Degree').order_by('year')
 

  context={
    'ps': ps_filtered,
    'ps2':ps_filtered_2
  }
  
  return render(request,'inst-wise.html',context)
