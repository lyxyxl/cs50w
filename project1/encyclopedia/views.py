from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import util
from . import apps

from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert(request, entry):
    markdowner = Markdown()
    page = markdowner.convert(entry)
    return render(request, "encyclopedia/entry.html", {
        "page": page
    })

def title(request, name):
    entry = util.get_entry(name)
    if entry is None:
        return render(request, "encyclopedia/error.html")
    else:
        return convert(request,entry)

def search(request):
    if request.method == "POST":
       form = apps.SearchForm(request.POST)
       if form.is_valid():
           q = form.cleaned_data["q"]
           return HttpResponseRedirect(q)
    else:
        form = apps.SearchForm()
    return index(request)
           
def results(request, q):
    search = util.get_entry(q)
    if search is None:
        return render(request, "encyclopedia/index.html", {
            "q": q,
            "entries": util.list_entries()
        })
    else:
        return convert(request, search)
        
