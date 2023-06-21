from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("team/", views.team, name="team"),
    path("competition/", views.competition, name="competition"),
    path("register/", views.register, name="register"),
    path("make-payment/", views.makePayment, name="makePayment"),
]