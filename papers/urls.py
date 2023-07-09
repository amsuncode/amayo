from django.urls import path

from papers.views import PapersView

urlpatterns = [
    path("", PapersView.as_view(), name="papers"),
]