# Generated by Django 5.0.6 on 2024-06-08 23:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='doc_upload',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='image',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='notes',
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('doc_upload', models.FileField(blank=True, upload_to='uploads/%Y/%m/%d')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edited_by', to=settings.AUTH_USER_MODEL)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edited_lesson', to='parks.lesson')),
            ],
        ),
    ]