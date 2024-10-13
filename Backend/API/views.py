from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import City
from .serializers import CitySerializer

@api_view(["GET"])
def get_data(request):
	cities = City.objects.all()
	serializer = CitySerializer(cities, many=True)
	return Response(serializer.data)

@api_view(["POST"])
def add_data(request):
	serializer = CitySerializer(data=reques.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)