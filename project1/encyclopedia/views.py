from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, name):
    title = util.get_entry(name)
    if title is None:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    else:
        return render