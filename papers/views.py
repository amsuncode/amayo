from django.views import generic
from django.shortcuts import render, redirect

from .models import Paper #, Question

# from django.forms import PaperForm

class IndexView(generic.ListView):
    template_name = "papers/papers.html"

class CreatePaperView(generic.DetailView):
    template_name = "papers/create_question.html"
    model = Paper

# class AddQuestionView(generic.DetailView):
#     template_name = "papers/add_question.html"
#     model = Question

