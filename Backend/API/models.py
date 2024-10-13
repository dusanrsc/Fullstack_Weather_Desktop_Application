from django.db import models

# Create your models here.
class City(models.Model):
	name = models.CharField(max_length=200)
	cond = models.CharField(max_length=200)
	temp = models.IntegerField()
	wind = models.BooleanField(default=False)

	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"City: {self.name}, Created: {self.created}"