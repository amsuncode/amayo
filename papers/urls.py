from django.urls import path


from papers.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="papers"),
    # path("", IndexView.as_view(), name="papers"),
]