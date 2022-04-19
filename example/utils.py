from http.client import HTTPResponse

from .models import blog_content


def get(request):
    blog = blog_content.objects.all()
    return blog


def create(request):
    blog_content(author=request.POST.get("author"))
    blog_content.save()
    return HTTPResponse("ok")
