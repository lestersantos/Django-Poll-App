from django.shortcuts import get_object_or_404, render

from .models import Question
"""
Django view, is a type of web page, serves a specific function
an has a specific template.
"""

"""
EXPRESS VS DJANGO

Both req and res are made available to us by the Express framework. 
The req object represents the HTTP request and has properties for 
the request query string, parameters, body, and HTTP headers. 

When a page is requested, Django creates an HttpRequest object that 
contains metadata about the request. 
Then Django loads the appropriate view, passing the HttpRequest 
as the first argument to the view function
"""
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list,}
    return render(request, "polls/index.html",context)

"""
The get_object_or_404() takes a Django model as its first argument
and an arbitray numberof keywords arguments, which it
passes to the get() funciton of the model's manager
"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})    

def results(request, question_id):
    response = "result You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Vote You're voting on question %s." % question_id)