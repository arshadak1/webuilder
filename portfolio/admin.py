from django.contrib import admin
from .models import Template, TemplateJSFile, TemplateCSSFile, TemplateHTMLFile, TemplateIMGFile
# Register your models here.


class TemplateCSSFileAdmin(admin.StackedInline):
    model = TemplateCSSFile


class TemplateJSFileAdmin(admin.StackedInline):
    model = TemplateJSFile


class TemplateHTMLFileAdmin(admin.StackedInline):
    model = TemplateHTMLFile


class TemplateIMGFileAdmin(admin.StackedInline):
    model = TemplateIMGFile


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    inlines = [TemplateJSFileAdmin, TemplateCSSFileAdmin,
               TemplateHTMLFileAdmin, TemplateIMGFileAdmin]


@admin.register(TemplateJSFile)
class TemplateJSFileAdmin(admin.ModelAdmin):
    pass


@admin.register(TemplateCSSFile)
class TemplateCSSFileAdmin(admin.ModelAdmin):
    pass


@admin.register(TemplateHTMLFile)
class TemplateHTMLFileAdmin(admin.ModelAdmin):
    pass


@admin.register(TemplateIMGFile)
class TemplateIMGFileAdmin(admin.ModelAdmin):
    pass
