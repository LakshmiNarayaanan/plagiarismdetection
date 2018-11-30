from tastypie.resources import ModelResource
from checker.models import Data,Document


class DataResource(ModelResource):
	class Meta:
		queryset = Data.objects.all()
		resource_name = 'data'

class DocumentResource(ModelResource):
	class Meta:
		queryset = Document.objects.all()
		resource_name = 'document'
