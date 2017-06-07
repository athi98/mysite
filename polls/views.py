from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from polls.models import Question, Choice


def index(request):
    question = Question.objects.order_by('-pub_date')[:5]
    context = {'question': question}
    template = "polls/index.html"
    return render(request, template, context)

def question_details(request, id):
    question = Question.objects.get(id=int(id))
    context = {'question': question}
    template = "polls/question.html"
    return render(request, template, context)

def question_result(request, id):
    question = Question.objects.get(id=int(id))
    choices = Choice.objects.filter(question=question)
    context = {'question': question, 'choices':choices}
    template = "polls/result.html"
    return render(request, template, context)


def question_vote(request, id):
    question = Question.objects.get(id=int(id))
    if request.method == 'GET':
        choices = Choice.objects.filter(question=question)
        context = {'question': question, 'choices': choices}
        template = "polls/votes.html"
        return render(request, template, context)

    if request.method == "POST":
        id = int(request.POST['choice'])
        c = Choice.objects.get(id=id)
        c.vote += 1
        c.save()
        return redirect('view_result', question.id)








