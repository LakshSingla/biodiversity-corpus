from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt

from .serializers import CategorySerializer
from .models import Category, SubCategory

def construct_response_categories(all_categories):
    return {str(category): [str(sub_category) for sub_category in category.subcategory] for category in all_categories}

@csrf_exempt
def category(request):
    if request.method == 'GET':
        c = Category.objects.filter()
        return JsonResponse(construct_response_categories(c))

    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        if not (body['category_name'] and body['category_name'].strip()):
            return JsonResponse({"created": False})

        try:
            entry = Category.objects.get(name=body['category_name'])
            return JsonResponse({"created": False})
        except Category.DoesNotExist as e:
            Category.objects.create(name = body['category_name'].strip(), subcategory=[])
            return JsonResponse({"created": True})

@csrf_exempt
def sub_category(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        category_name = None
        subcategory_name = None
        try:
            category_name = body['category_name'].strip()
            subcategory_name = body['subcategory_name'].strip()
        except Exception:
            return JsonResponse({"created": False})
        
        if not (category_name and subcategory_name):
            return JsonResponse({"created": False})
        
        try:
            entry = Category.objects.get(name=category_name)
            sub_entry = SubCategory.objects.create(name = subcategory_name)
            # print(subcategory_name)
            print(sub_entry)
            sub_entry.save()
            entry.subcategory.append(sub_entry)
            entry.save()
            return JsonResponse({"created": True})
        
        except Category.DoesNotExist as e:
            return JsonResponse({"created": False})