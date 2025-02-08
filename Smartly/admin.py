from django.contrib import admin
from Smartly.models import Course , Tag , Prerequisite , Learning

# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin , LearningAdmin ,PrerequisiteAdmin]

admin.site.register(Course,CourseAdmin)
