import json
from django.http import JsonResponse
from .models import User


def new(request):
    data = json.loads(request.body.decode("utf-8"))
    username = data['user']
    password = data['pass']
    if not User.objects.filter(username=username):
        User.objects.create(username=username, password=password)
        return JsonResponse({
            'status': 'success',
        })
    else:
        return JsonResponse({
            'status': 'failed',
        })


def login(request):
    data = json.loads(request.body.decode("utf-8"))
    username = data['user']
    password = data['pass']
    if User.objects.filter(username=username, password=password):
        return JsonResponse({
            'status': 'success',
        })
    else:
        return JsonResponse({
            'status': 'failed',
        })
