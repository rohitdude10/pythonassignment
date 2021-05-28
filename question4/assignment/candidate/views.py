import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student, Test_score
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User


@api_view(['POST'])
def add_candidate(request):
    print(request.data)
    Student.objects.create(
        name=request.data["name"], email=request.data["email"])
    # allstudent= Student.objects.values()
    return Response("allstudent")


@api_view(["POST"])
def add_score(request):
    choosenstudent = Student.objects.get(id=request.data["id"])
    Test_score(student=choosenstudent,  first_round=request.data["first"],
               second_round=request.data["second"], third_round=request.data["third"]).save()

    return Response("student score add")


@api_view(["GET"])
def get_best(request):

    all = Test_score.objects.values().values()
    print(all)

    student_mark = {}
    for user in all:
        mark = 0
        studentid = user["id"]
        mark = user["first_round"] + user["second_round"] + user["third_round"]
        student_mark[studentid] = mark
    best_student= max(student_mark, key=student_mark.get)
    best_student_name= Student.objects.values().filter(id=best_student)

    return Response(best_student_name)

@api_view(["GET"])
def get_avg(request):
    pass
    all = Test_score.objects.values().values()
    first_avg=0
    second_avg=0
    third_avg=0
    for user in all:
        first_avg=first_avg+user["first_round"]
        second_avg= second_avg+user["second_round"]
        third_avg= third_avg +user["third_round"]
    return JsonResponse({"first_avg":first_avg,"second_avg": second_avg,"third_avg": third_avg})

@api_view(['POST'])
def creating_user(request):
    data = request.data
    # data = JSONParser().parse(newdata)
    # print(data)
    user = User.objects.create_superuser(data["username"], data["password"]) 
    user.save()
    return Response("user is created")
