"""gardastations URL Configuration

Written with reference to the Django Rest Framework tutorials on www.django-rest-framework.org/
Most notably http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

"""
from django.conf.urls import url
from django.contrib.gis import admin
from rest_framework.urlpatterns import format_suffix_patterns
from stations.views import *

station_list = StationViewSet.as_view({
    'get': 'list'
})
station_detail = StationViewSet.as_view({
    'get': 'retrieve'

})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

burglary_list = BurglaryViewSet.as_view({
    'get': 'list'
})
burglary_detail = BurglaryViewSet.as_view({
    'get': 'retrieve'
})
dangacts_list = DangActsViewSet.as_view({
    'get': 'list'
})
dangacts_detail = DangActsViewSet.as_view({
    'get': 'retrieve'
})
drugs_list = DrugsViewSet.as_view({
    'get': 'list'
})
drugs_detail = DrugsViewSet.as_view({
    'get': 'retrieve'
})
fraud_list = FraudViewSet.as_view({
    'get': 'list'
})
fraud_detail = FraudViewSet.as_view({
    'get': 'retrieve'
})
govmnt_list = GovmntViewSet.as_view({
    'get': 'list'
})
govmnt_detail = GovmntViewSet.as_view({
    'get': 'retrieve'
})
kidnap_list = KidnapViewSet.as_view({
    'get': 'list'
})
kidnap_detail = KidnapViewSet.as_view({
    'get': 'retrieve'
})
property_list = PropertyViewSet.as_view({
    'get': 'list'
})
property_detail = PropertyViewSet.as_view({
    'get': 'retrieve'
})
robbery_list = RobberyViewSet.as_view({
    'get': 'list'
})
robbery_detail = RobberyViewSet.as_view({
    'get': 'retrieve'
})
social_list = SocialViewSet.as_view({
    'get': 'list'
})
social_detail = SocialViewSet.as_view({
    'get': 'retrieve'
})
theft_list = TheftViewSet.as_view({
    'get': 'list'
})
theft_detail = TheftViewSet.as_view({
    'get': 'retrieve'
})
threats_list = ThreatsViewSet.as_view({
    'get': 'list'
})
threats_detail = ThreatsViewSet.as_view({
    'get': 'retrieve'
})
weapons_list = WeaponsViewSet.as_view({
    'get': 'list'
})
weapons_detail = WeaponsViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^stations/$', station_list, name='station-list'),
    url(r'^stations/(?P<pk>[0-9]+)/$', station_detail, name='gardastations-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^burglary/$', burglary_list, name='burglary-list'),
    url(r'^burglary/(?P<pk>[0-9]+)/$', burglary_detail, name='burglary-detail'),
    url(r'^dangacts/$', dangacts_list, name='dangacts-list'),
    url(r'^dangacts/(?P<pk>[0-9]+)/$', dangacts_detail, name='dangacts-detail'),
    url(r'^drugs/$', drugs_list, name='drugs-list'),
    url(r'^drugs/(?P<pk>[0-9]+)/$', drugs_detail, name='drugs-detail'),
    url(r'^fraud/$', fraud_list, name='fraud-list'),
    url(r'^fraud/(?P<pk>[0-9]+)/$', fraud_detail, name='fraud-detail'),
    url(r'^govmnt/$', govmnt_list, name='govmnt-list'),
    url(r'^govmnt/(?P<pk>[0-9]+)/$', govmnt_detail, name='govmnt-detail'),
    url(r'^kidnap/$', kidnap_list, name='kidnap-list'),
    url(r'^kidnap/(?P<pk>[0-9]+)/$', kidnap_detail, name='kidnap-detail'),
    url(r'^property/$', property_list, name='property-list'),
    url(r'^property/(?P<pk>[0-9]+)/$', property_detail, name='property-detail'),
    url(r'^robbery/$', robbery_list, name='robbery-list'),
    url(r'^robbery/(?P<pk>[0-9]+)/$', robbery_detail, name='robbery-detail'),
    url(r'^social/$', social_list, name='social-list'),
    url(r'^social/(?P<pk>[0-9]+)/$', social_detail, name='social-detail'),
    url(r'^theft/$', theft_list, name='theft-list'),
    url(r'^theft/(?P<pk>[0-9]+)/$', theft_detail, name='theft-detail'),
    url(r'^threats/$', threats_list, name='threats-list'),
    url(r'^threats/(?P<pk>[0-9]+)/$', threats_detail, name='threats-detail'),
    url(r'^weapons/$', weapons_list, name='weapons-list'),
    url(r'^weapons/(?P<pk>[0-9]+)/$', weapons_detail, name='weapons-detail'),
    url(r'^admin/', admin.site.urls),
])