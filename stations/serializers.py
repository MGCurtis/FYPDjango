"""

Written with reference to the Django Rest Framework tutorials on www.django-rest-framework.org/
Most notably http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/

"""
from django.contrib.auth.models import User
from rest_framework import serializers
from stations.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class StationSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = GardaStations
        fields = ('url', 'id', 'fid', 'name', 'blank', 'Sun', 'Address',
                  'Longitude', 'Latitude', 'County', 'Phone', 'StationID',
                  'Station', 'Mon_Fri', 'Sat')

class BurglarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Burglary
        fields = ('v2003', 'v2004', 'v2005', 'v2006', 'v2007', 'v2008', 'v2009', 'v2010',
                  'v2011', 'v2012', 'v2013', 'v2014', 'v2015', 'v2016', 'name')

class DangActsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DangActs
        fields = ('v2003', 'v2004', 'v2005', 'v2006', 'v2007', 'v2008', 'v2009', 'v2010',
                  'v2011', 'v2012', 'v2013', 'v2014', 'v2015', 'v2016', 'name')

class DrugsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drugs
        fields = ('v2003', 'v2004', 'v2005', 'v2006', 'v2007', 'v2008', 'v2009', 'v2010',
                  'v2011', 'v2012', 'v2013', 'v2014', 'v2015', 'v2016', 'name')

class FraudSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fraud
        fields = ('v2003', 'v2004', 'v2005', 'v2006', 'v2007', 'v2008', 'v2009', 'v2010',
                  'v2011', 'v2012', 'v2013', 'v2014', 'v2015', 'v2016', 'name')

class GovmntSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Govmnt
        fields = ('v2003', 'v2004', 'v2005', 'v2006', 'v2007', 'v2008', 'v2009', 'v2010',
                  'v2011', 'v2012', 'v2013', 'v2014', 'v2015', 'v2016', 'name')

class KidnapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kidnap
        fields = ('v2003', 'v2004', 'v2005', 'v2006', 'v2007', 'v2008', 'v2009', 'v2010',
                  'v2011', 'v2012', 'v2013', 'v2014', 'v2015', 'v2016', 'name')

class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ('v2003', 'v2004', 'v2005', 'v2006', 'v2007', 'v2008', 'v2009', 'v2010',
                  'v2011', 'v2012', 'v2013', 'v2014', 'v2015', 'v2016', 'name')


class RobberySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Robbery
        fields = ('v2003', 'v2004', 'v2005', 'v2006', 'v2007', 'v2008', 'v2009', 'v2010',
                  'v2011', 'v2012', 'v2013', 'v2014', 'v2015', 'v2016', 'name')


class SocialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Social
        fields = ('v2003', 'v2004', 'v2005', 'v2006', 'v2007', 'v2008', 'v2009', 'v2010',
                  'v2011', 'v2012', 'v2013', 'v2014', 'v2015', 'v2016', 'name')


class TheftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theft
        fields = ('v2003', 'v2004', 'v2005', 'v2006', 'v2007', 'v2008', 'v2009', 'v2010',
                  'v2011', 'v2012', 'v2013', 'v2014', 'v2015', 'v2016', 'name')


class ThreatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Threats
        fields = ('v2003', 'v2004', 'v2005', 'v2006', 'v2007', 'v2008', 'v2009', 'v2010',
                  'v2011', 'v2012', 'v2013', 'v2014', 'v2015', 'v2016', 'name')


class WeaponsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weapons
        fields = ('v2003', 'v2004', 'v2005', 'v2006', 'v2007', 'v2008', 'v2009', 'v2010',
                  'v2011', 'v2012', 'v2013', 'v2014', 'v2015', 'v2016', 'name')