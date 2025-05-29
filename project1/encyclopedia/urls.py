from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.find, name="entry"),
    path("search/", views.search, name='search'),
    path("search/<str:q>", views.results, name='results'),
    path("new/", views.new, name="new"),
    path("<str:title>/edit/", views.edit, name="edit"),
    path("random/", views.random, name="random")
]
