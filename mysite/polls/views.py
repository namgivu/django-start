# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.http import HttpResponse
from models import Question


def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in questions])
    return HttpResponse(output)


def detail(request, question_id):
  return HttpResponse('Detail of question %s.' % question_id)


def results(request, question_id):
  return HttpResponse('Result of question %s.' % question_id)


def vote(request, question_id):
  return HttpResponse('Voting on question %s.' % question_id)

