from django.shortcuts import render

from . import util

from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):
    title = util.get_entry(name)
    if title is None:
        return render(request, "encyclopedia/error.html")
    markdowner = Markdown()
    page = markdowner.convert(title)
    return render(request, "encyclopedia/entry.html", {
        "page": page
    })
