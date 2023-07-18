from django.views.generic.base import TemplateView
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from .forms import SignUpForm
from django.shortcuts import render


class HomePageView(View):
    template_name = "home/home.html"
    def get(self, request):
        return render(request, self.template_name)