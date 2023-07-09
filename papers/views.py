from django.views.generic.base import TemplateView

class PapersView(TemplateView):
    template_name = "papers/papers.html"