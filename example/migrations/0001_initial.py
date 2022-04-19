# Generated by Django 3.2.9 on 2022-04-18 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_content',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=500)),
                ('category', models.CharField(default='', max_length=500)),
                ('description', models.TextField(default='')),
                ('image', models.CharField(default='', max_length=500)),
                ('status', models.CharField(default='', max_length=50)),
                ('date_modified', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='other',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ok', models.CharField(default='', max_length=500)),
                ('blog', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='example.blog_content')),
            ],
        ),
    ]