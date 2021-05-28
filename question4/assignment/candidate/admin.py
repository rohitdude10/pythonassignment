from django.contrib import admin
from .models import Student, Test_score

@admin.register(Student,Test_score)
class AuthorAdmin(admin.ModelAdmin):
    pass