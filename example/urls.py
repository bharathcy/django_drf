# Create your tests here.
from django.urls import path

from .apiviews import CreateAPI, BlogList
from .views import *

urlpatterns = [
    path("", blog_content_view, name="blog-content-view"),
    path("blogs/", BlogList, name="blog-list"),
    path("create/", create_view, name="blog-create"),
    path("api-create/", CreateAPI, name="blog-list-api"),

]
