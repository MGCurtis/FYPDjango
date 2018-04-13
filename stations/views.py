"""

Written with reference to the Django Rest Framework tutorials on www.django-rest-framework.org/
Most notably http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

"""

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from stations.serializers import  *
from stations.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse



# Create your views here.


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StationViewSet(viewsets.ModelViewSet):
    queryset = GardaStations.objects.all()
    serializer_class = StationSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class BurglaryViewSet(viewsets.ModelViewSet):
    queryset = Burglary.objects.all()
    serializer_class = BurglarySerializer

class DangActsViewSet(viewsets.ModelViewSet):
    queryset = DangActs.objects.all()
    serializer_class = DangActsSerializer

class DrugsViewSet(viewsets.ModelViewSet):
    queryset = Drugs.objects.all()
    serializer_class = DrugsSerializer

class FraudViewSet(viewsets.ModelViewSet):
    queryset = Fraud.objects.all()
    serializer_class = FraudSerializer

class GovmntViewSet(viewsets.ModelViewSet):
    queryset = Govmnt.objects.all()
    serializer_class = GovmntSerializer

class KidnapViewSet(viewsets.ModelViewSet):
    queryset = Kidnap.objects.all()
    serializer_class = KidnapSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class RobberyViewSet(viewsets.ModelViewSet):
    queryset = Robbery.objects.all()
    serializer_class = RobberySerializer

class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer

class TheftViewSet(viewsets.ModelViewSet):
    queryset = Theft.objects.all()
    serializer_class = TheftSerializer

class ThreatsViewSet(viewsets.ModelViewSet):
    queryset = Threats.objects.all()
    serializer_class = ThreatsSerializer

class WeaponsViewSet(viewsets.ModelViewSet):
    queryset = Weapons.objects.all()
    serializer_class = WeaponsSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'stations': reverse('station-list', request=request, format=format),
        'burglary': reverse('burglary-list', request=request, format=format),
        'dangerous acts': reverse('dangacts-list', request=request, format=format),
        'drugs': reverse('drugs-list', request=request, format=format),
        'fraud': reverse('fraud-list', request=request, format=format),
        'government': reverse('govmnt-list', request=request, format=format),
        'kidnapping': reverse('kidnap-list', request=request, format=format),
        'property': reverse('property-list', request=request, format=format),
        'robbery': reverse('robbery-list', request=request, format=format),
        'social': reverse('social-list', request=request, format=format),
        'theft': reverse('theft-list', request=request, format=format),
        'threats': reverse('threats-list', request=request, format=format),
        'weapons': reverse('weapons-list', request=request, format=format)
    })