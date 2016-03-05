from django.shortcuts import render
from opendataday.models import CongressMan, Restaurant, CongressRestaurantMap
from django.http import JsonResponse, HttpResponse
# Create your views here.

def get_data(request):
    result = {"data":[]}
    try:
        maps = CongressRestaurantMap.members.all()
    except:
        pass
    str = """
{
    data: [
        {
            restaurant_name: "식당이름",
            latitude: 1.1,
            longitude: 1.1,
            category: "한식",
            visitied: [{
                party: "정당",
                congressman_name: "의원이름",
                local: "지역구",
                price: 111
            }, {
                party: "정당",
                congressman_name: "의원이름",
                local: "지역구",
                price: 111
            }]
        }, {
            restaurant_name: "식당이름",
            latitude: 1.1,
            longitude: 1.1,
            category: "한식",
            visitied: [{
                party: "정당",
                congressman_name: "의원이름",
                local: "지역구",
                price: 111
            }, {
                party: "정당",
                congressman_name: "의원이름",
                local: "지역구",
                price: 111
            }]
        }
    ]
}
"""
    return HttpResponse(str)
    # return JsonResponse(result)