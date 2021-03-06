# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Timestamp(models.Model):
    month = models.PositiveIntegerField('month', default=1)
    day = models.PositiveIntegerField('day', default=1)
    beginTime = models.FloatField(default=10)
    endTime = models.FloatField(default=10)
    timeLength = models.FloatField(default=10)
