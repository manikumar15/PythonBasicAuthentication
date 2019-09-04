from django.db import models

class Data(models.Model):
	empid=models.IntegerField(primary_key=True)
	empname=models.CharField(max_length=40)
	salary=models.IntegerField()

	def __str__(self):
		return self.empname