from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from .models import *

# Create your views here.


def index(request):
    context = {
        'all_snakes': Snake.objects.all()
    }
    return render(request, 'index.html', context)


def snakeForm(request):
    return render(request, 'snakeform.html')


def addSnake(request):
    if('venomous' in request.POST):
        ven = True
    else:
        ven = False
    errors = Snake.objects.snake_validate(request.POST)
    if len(errors) > 0:
        for tags, value in errors.items():
            messages.error(request, value, extra_tags=tags)
        return redirect("/snakes/new")
    newSnake = Snake.objects.create(
        name=request.POST['name'], length=request.POST['length'], venomous=ven)
    return redirect(f"/snakes/{newSnake.id}")


def oneSnake(request, snake_id):
    context = {
        'snake': Snake.objects.get(id=snake_id)
    }
    return render(request, 'newsnake.html', context)


def oneSnakeAjax(request, snake_id):
    snake = serializers.serialize(
        'json', Snake.objects.filter(id=snake_id))

    return JsonResponse(snake, safe=False)


def allSnakes(request):
    context = {
        'all_snakes': Snake.objects.all()
    }
    return render(request, "allsnakes.html", context)


def allSnakesAjax(request):
    allSnakes = serializers.serialize('json', Snake.objects.all())

    return JsonResponse(allSnakes, safe=False)


def deleteSnake(request, snake_id):
    Snake.objects.get(id=snake_id).delete()
    return redirect("/snakes/all")


def snakeFormAjax(request):
    return render(request, 'ajaxform.html')


def addSnakeAjax(request):
    if('venomous' in request.POST):
        ven = True
    else:
        ven = False
    errors = Snake.objects.snake_validate(request.POST)
    if len(errors) > 0:
        for tags, value in errors.items():
            messages.error(request, value, extra_tags=tags)
    else:
        Snake.objects.create(
            name=request.POST['name'], length=request.POST['length'], venomous=ven)
    return render(request, "ajaxform.html")


def deleteSnakeAjax(request, snake_id):
    Snake.objects.get(id=snake_id).delete()

    return JsonResponse({"message": "Success"})
