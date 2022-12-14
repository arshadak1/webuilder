# Generated by Django 4.1.2 on 2022-10-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=200, null=True, verbose_name='Template Name')),
                ('javascript', models.FileField(upload_to='js')),
                ('css', models.FileField(upload_to='css')),
                ('html', models.FileField(upload_to='html')),
                ('image', models.ImageField(upload_to='img')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
