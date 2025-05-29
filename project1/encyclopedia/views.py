from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from random import randint

from . import util
from . import apps

from markdown2 import Markdown

def index(request):
    entries = []
    fileentries = util.list_entries()
    for entry in fileentries:
        entries.append(entry.replace('_', ' '))
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def convert(request, entry, title):
    markdowner = Markdown()
    page = markdowner.convert(entry)
    return render(request, "encyclopedia/entry.html", {
        "page": page,
        "title": title
    })

def find(request, name):
    filename = name.replace(' ', '_')
    entry = util.get_entry(filename)
    if entry is None:
        return render(request, "encyclopedia/error.html", {
            "errormessage": "The page you are looking for does not exist! :/"
        })
    else:
        return convert(request, entry, name)

def search(request):
    if request.method == "POST":
        form = apps.SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data["q"]
            if q.isalpha():
                if q in util.list_entries():
                    return redirect(reverse("entry", kwargs={"name": q}))
                else:
                    return redirect(reverse("results", kwargs={"q": q}))
            else:
                return render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries(),
                    "inputmessage": "Invalid input"
                })
    else:
        form = apps.SearchForm()
    return index(request)
           
def results(request, q):
    search = util.get_entry(q)
    if search is None:
        result = []
        entries = util.list_entries()
        for entry in entries:
            if q in entry.lower():
                result.append(entry)
        if len(result) != 0:
            return render(request, "encyclopedia/index.html", {
                "q": q,
                "entries": result
            })
        else:
            return render(request, "encyclopedia/index.html", {
                "q": q,
                "resultmessage": "No results :/"
            })
    else:
        return convert(request, search, q)
        
def create(request, message=None):
    return render(request, "encyclopedia/create.html", {
        "createmessage": message
    })

def new(request):
    if request.method == "POST":
        form = apps.CreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if not all(char.isalpha() or char == ' ' for char in title):
                return create(request, "Invalid Title")
            elif title in util.list_entries():
                return create(request, "This page already exists!")
            else:
                filetitle = title.replace(' ', '_')
                util.save_entry(filetitle, content)
                return redirect(reverse("entry", kwargs={"name": filetitle}))
        else:
            return create(request, "All fields are required.")
    else:
        form = apps.CreateForm()
    return create(request)

def edit(request, title):
    if request.method == "POST":
        form = apps.EditForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return redirect(reverse("entry", kwargs={"name": title}))
    else:
        form = apps.EditForm()
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": util.get_entry(title)
    })

def random(request):
    entries = util.list_entries()
    entry = entries[randint(0, len(entries)-1)]
    return redirect(reverse("entry", kwargs={"name": entry}))