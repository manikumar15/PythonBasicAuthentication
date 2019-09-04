from rest_framework.serializers import ModelSerializer
from .models import Data

class Dataserializer(ModelSerializer):
	class Meta:
		model=Data
		fields='__all__'