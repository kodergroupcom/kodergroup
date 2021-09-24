from django.contrib import admin

from koderapp.models import (
    Info,
    Project,
    InCoding,
    BestQuestions,
    About,
    )

# Register your models here.

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('number', 'email','address','created_at')
    list_filter = ('number', 'email','address','created_at')
    search_fields = ('number', 'email','address','created_at')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'img','created_at')
    list_filter = ('name', 'img','created_at')
    search_fields = ('name', 'img','created_at')

@admin.register(InCoding)
class InCodingAdmin(admin.ModelAdmin):
    list_display = ('name','created_at')
    list_filter = ('name', 'created_at')
    search_fields = ('name','created_at')

@admin.register(BestQuestions)
class BestQuestionsAdmin(admin.ModelAdmin):
    list_display = ('question','created_at')
    list_filter = ('question', 'created_at')
    search_fields = ('question','created_at')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('about','created_at')
    list_filter = ('about', 'created_at')
    search_fields = ('about','created_at')
