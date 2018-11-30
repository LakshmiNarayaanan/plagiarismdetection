from tastypie.resources import ModelResource
from checker.models import Data

class DataResource(ModelResource):
	class Meta:
		queryset = Data.objects.all()
		resource_name = 'data'
