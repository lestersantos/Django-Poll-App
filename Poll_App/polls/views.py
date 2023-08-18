from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
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

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

"""
The get_object_or_404() takes a Django model as its first argument
and an arbitray numberof keywords arguments, which it
passes to the get() function of the model's manager

pk stands for primary key
"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})    

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html",{"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(request.POST)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        # return HttpResponse("Vote You're voting on question %s." % question_id)