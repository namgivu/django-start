# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.http import HttpResponse
from models import Question
from django.shortcuts import get_object_or_404


def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  output = ', '.join([q.question_text for q in latest_question_list])
  return HttpResponse(output)


def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  return render(request, 'polls/index.html', context = {
    'latest_question_list': latest_question_list,
  })


def detail(request, question_id):
  return HttpResponse('Detail of question %s.' % question_id)


def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id) #also we have get_object_or_404()
  return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
  return HttpResponse('Result of question %s.' % question_id)


def vote(request, question_id):
  return HttpResponse('Voting on question %s.' % question_id)

