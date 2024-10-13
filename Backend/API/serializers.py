from rest_framework import serializers
from .models import City

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = ["name", "cond", "temp", "wind"] # or "__all__" for all fields