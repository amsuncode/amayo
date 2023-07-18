from django.http import Http404
from django.views import generic
from django.views import View
from django.shortcuts import render, redirect
from django.utils import timezone

from django.contrib.auth.decorators import login_required

from .models import Paper 

app_name = 'papers'
# from django.forms import PaperForm
# @login_required(login_url="/login")
class IndexView(View):
    def get(self, request):
        papers = Paper.objects.all().order_by('-created')
        context = {'papers': papers}
        return render(request, 'papers/papers.html', context)

class DetailView(View):
    def get(self, request, pk):
        paper = Paper.objects.get(id=pk)
        context = {'paper': paper}
        return render(request, 'papers/papers.html', context)