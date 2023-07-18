from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

from papers.views import IndexView, DetailView

urlpatterns = [
    path("", (IndexView.as_view()), name="papers"),
    path('<int:pk>/', DetailView.as_view(), name="detail"),
]
