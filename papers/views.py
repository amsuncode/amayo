from django.http import Http404
from django.views import generic
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Paper 

# from django.forms import PaperForm

class IndexView(generic.ListView):
    template_name = "papers/papers.html"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Paper.objects.filter(
        created__lte=timezone.now()
        ).order_by('-created')[:5]

class CreatePaperView(generic.DetailView):
    template_name = "papers/create_question.html"

# class AddQuestionView(generic.DetailView):
#     template_name = "papers/add_question.html"
#     model = Question

