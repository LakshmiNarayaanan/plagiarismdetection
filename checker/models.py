import uuid
import os
from django.db import models
from django.contrib.auth.models import User
randomid = uuid.uuid4()
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (randomid, ext)
    return os.path.join('documents/', filename)


class Data(models.Model):
    data = models.TextField()
    user = models.ForeignKey(User,null=True)
    def __str__(self):
        return self.data

	# keywords = models.CharField(max_length=500)
#
# class Document(models.Model):
    #document = models.FileField(upload_to=get_file_path)

	#uploaded_at = models.DateTimeField(auto_now_add=True)
class Document(models.Model):

    user = models.ForeignKey(User,null=True)
    result = models.DecimalField(max_digits=50,decimal_places=5,null=True)

    description = models.CharField(max_length=255, blank=True, default='')
    document = models.CharField(max_length=255, )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.document
