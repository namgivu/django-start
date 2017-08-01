# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date      = models.DateTimeField('date published') #an optional first-positional-argument to giv a human-readable name


class Choice(models.Model):
  choice_text = models.CharField(max_length=200)
  votes       = models.IntegerField(default=0)

  question = models.ForeignKey(Question, on_delete=models.CASCADE)
