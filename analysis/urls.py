from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from analysis import views

urlpatterns = [
    url(r'^mythril/v1/analysis/$', views.bytecode_submission),
    url(r'^mythril/v1/analysis/(?P<uuid>[0-9a-f-]+)$', views.status),
    url(r'^mythril/v1/analysis/(?P<uuid>[0-9a-f-]+)/issues/$', views.report)
]

urlpatterns = format_suffix_patterns(urlpatterns)