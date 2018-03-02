from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProviderList, ProviderDetail

urlpatterns = [
    url(r'^providers/$', ProviderList.as_view()),
    url(r'^providers/(?P<pk>[0-9]+)/$', ProviderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
