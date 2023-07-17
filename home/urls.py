from django.urls import path

from home.views import HomePageView, LogoutUser, RegisterView , LoginView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutUser.as_view(), name="logout"),
    path("accounts/register/", RegisterView.as_view(), name="register"),
]