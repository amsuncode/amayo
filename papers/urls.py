from django.urls import path
from django.contrib.auth.decorators import login_required

from papers.views import IndexView, CreatePaperView

urlpatterns = [
    path("", login_required(IndexView.as_view()), name="papers"),
    path("create/", login_required(CreatePaperView.as_view()), name="create_paper"),
    # Other URL patterns
]
