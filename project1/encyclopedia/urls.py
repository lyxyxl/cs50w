from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.title, name="entry"),
    path("search/", views.search, name='search'),
    path("search/<str:q>", views.results, name='results'),
    path("create/", views.create, name="create")
]
