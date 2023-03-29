from django.shortcuts import render
from django.http import HttpResponse

from .models import ToDoList, Item

from .forms import CreateNewList

# Create your views here.


def index(resp, ind):
    ls = ToDoList.objects.get(id=ind)

    return render(resp, "main/list.html", {"ls": ls})


def home(resp):
    return render(resp, "main/home.html", {})


def create(resp):
    if resp.method == "POST":
        form = CreateNewList(resp.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
    else:
        form = CreateNewList()

    return render(resp, "main/create.html", {"form": form})
