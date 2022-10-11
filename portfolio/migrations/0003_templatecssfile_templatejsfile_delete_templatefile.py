# Generated by Django 4.1.2 on 2022-10-06 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_template_created_remove_template_css_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateCSSFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('css', models.FileField(upload_to='css')),
                ('html', models.FileField(upload_to='html')),
                ('image', models.ImageField(upload_to='img')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.template')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateJSFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('javascript', models.FileField(upload_to='js')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.template')),
            ],
        ),
        migrations.DeleteModel(
            name='TemplateFile',
        ),
    ]
