# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return HttpResponse('This is polls index.')


def detail(request, question_id):
  return HttpResponse('Detail of question %s.' % question_id)


def results(request, question_id):
  return HttpResponse('Result of question %s.' % question_id)


def vote(request, question_id):
  return HttpResponse('Voting on question %s.' % question_id)

