from django.contrib.auth.models import User
from django.db import models


class blog_content(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author', null=True)
    title = models.CharField(default='', max_length=500)
    category = models.CharField(default='', max_length=500)
    description = models.TextField(default='')
    image = models.CharField(default='', max_length=500)
    status = models.CharField(default='', max_length=50)
    date_modified = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def _str_(self):
        return str(self.id)


class other(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(blog_content, on_delete=models.CASCADE, default=1)
    ok = models.CharField(default='', max_length=500)
