from django.shortcuts import render
from django.http import JsonResponse

def tweets(request, keyword):
    return JsonResponse({
        "keyword": keyword
    })
