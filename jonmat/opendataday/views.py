from django.shortcuts import render
from opendataday.models import CongressMan, Restaurant, CongressRestaurantMap
from django.http import JsonResponse
# Create your views here.

def get_data(request):
    result = {"data":[]}
    try:
        maps = CongressRestaurantMap.members.all()
    except:
        pass
    return JsonResponse(result)