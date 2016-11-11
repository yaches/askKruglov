from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

app_name = 'askKruglov_app'
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	# url(r'^$', RedirectView.as_view(url='1')),
	url(r'^(?P<page_num>[0-9]+)$', views.index, name = 'index'),
	url(r'^hot/$', views.hot, name = 'hot'),
	url(r'^hot/(?P<page_num>[0-9]+)$', views.hot, name = 'hot'),
	url(r'^tag/(?P<tag_name>[-\w]+)$', views.tag, name = 'tag'),
	url(r'^tag/(?P<tag_name>[-\w]+)/(?P<page_num>[0-9]+)$', views.tag, name = 'tag'),
	url(r'^question/(?P<question_id>[0-9]+)$', views.question, name = 'question'),
	url(r'^question/(?P<question_id>[0-9]+)/(?P<page_num>[0-9]+)$', views.question, name = 'question'),
]