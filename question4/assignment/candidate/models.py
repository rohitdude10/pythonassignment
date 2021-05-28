from django.db import models
from django.db.models.base import ModelBase
from django.db.models.fields import CharField, EmailField, IntegerField
from django.db.models.lookups import In


class Student(models.Model):
    name = CharField(max_length=254, null=True)
    email = EmailField(max_length=254, null=True)


class Test_score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    first_round = IntegerField(null=True)
    second_round = IntegerField(null=True)
    third_round = IntegerField(null=True)
