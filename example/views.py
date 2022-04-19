from django.shortcuts import render

from .utils import *


def blog_content_view(request):
    return render(request,"index.html", {"data": get(request)})


def create_view(request):
    return render(request,"index.html", {"data": create(self="", request=request)})
