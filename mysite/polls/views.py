# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def index(request):
  from django.http import HttpResponse
  return HttpResponse("Hello, world. You're at the polls index.")
