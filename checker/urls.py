from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import Check
import re
import login.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$',Check.as_view()),
	url(r'^login/', login.views.user_login,name='login'),
	url(r'^logout/', login.views.logout_page	),
	url(r'^contact	/', login.views.logout_page	),
	url(r'^register/', login.views.register),
    url(r'^plagchecker',views.geturls,name='geturls'),
	url(r'^upload/$', views.model_form_upload, name='model_form_upload'),
	url(r'^show/(.*)/$',views.show,name='show'),
	url(r'^dashboard/',views.dashboard,name='dashboard')
	]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
