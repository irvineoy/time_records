# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Timestamp
import partTime

# Create your views here.
def index(request):
    user_list = []
    sumTime = 0
    time_list = Timestamp.objects.all()
    for oneday in time_list:
        user_list.append(oneday)
        sumTime += oneday.timeLength

    if request.method == "POST":
        month = request.POST.get("month", None)
        day = request.POST.get("day", None)
        beginTime = request.POST.get("beginTime", None)
        endTime = request.POST.get("endTime", None)
        timeLength = float(endTime) - float(beginTime)
        temp = {"month":month, "day":day, "beginTime":beginTime, "endTime":endTime, "timeLength":timeLength}
        sumTime = 0
        user_list = []
        Timestamp.objects.create(**temp)
        time_list = Timestamp.objects.all()
        #for oneday in time_list:
        #    user_list.append(oneday)
        #    sumTime += oneday.timeLength
    #totalMoney = sumTime * 880
    user_list = partTime.showTimeModule(time_list)
    sumTime = 0
    for oneday in user_list:
        sumTime += oneday.timeLength
    totalMoney = sumTime * 880
    return render(request, "index.html", {
        "data":user_list, 
        "sumTime":sumTime,
        "totalMoney":totalMoney
        })
