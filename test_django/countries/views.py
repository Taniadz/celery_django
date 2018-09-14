from django.shortcuts import render
from django.http import JsonResponse
from .models import Country

# Create your views here.
def countries(request):
    countries = list(Country.objects.values())
    return JsonResponse(countries, safe=False)