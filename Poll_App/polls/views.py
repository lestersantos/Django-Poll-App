from django.http import HttpResponse

from .models import Question
"""
Django view, is a type of web page, serves a specific function
an has a specific template.
"""
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("detail You're looking at question %s." % question_id)

def results(request, question_id):
    response = "result You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Vote You're voting on question %s." % question_id)