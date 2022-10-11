
from django.db import models
import os
# Create your models here.


class Template(models.Model):
    template_name = models.CharField(
        max_length=200, null=True, blank=False, verbose_name='Template Name')

    def __str__(self):
        return self.template_name


class TemplateJSFile(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    javascript = models.FileField(upload_to='js', null=False, blank=False)

    def filename(self):
        return os.path.basename(self.javascript.name)


class TemplateCSSFile(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    css = models.FileField(upload_to='css', null=False, blank=False)

    def filename(self):
        return os.path.basename(self.css.name)

class TemplateHTMLFile(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    html = models.FileField(upload_to='html', null=False, blank=False)


    def filename(self):
        return os.path.basename(self.html.name)

class TemplateIMGFile(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img', null=False, blank=False)

    def filename(self):
        return os.path.basename(self.image.name)
