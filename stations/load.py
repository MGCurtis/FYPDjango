import os
from django.contrib.gis.utils import LayerMapping
from .models import GardaStations, Burglary, DangActs, Drugs, Fraud, Govmnt, Kidnap, Property, Robbery, Social, Theft, Threats, Weapons

station_mapping = {
    'fid' : 'fid',
    'name' : 'Name',
    'blank' : '_',
    'Sun' : 'Sun',
    'Address' : 'Address',
    'Longitude' : 'Longitude',
    'County' : 'County',
    'Phone' : 'Phone',
    'StationID' : 'Station',
    'Mon_Fri' : 'Mon_Fri',
    'Latitude' : 'Latitude',
    'Sat' : 'Sat',
    'point' : 'POINT',
}

burglary_mapping = {
    'v2003' : '2003',
    'v2004' : '2004',
    'v2005' : '2005',
    'v2006' : '2006',
    'v2007' : '2007',
    'v2008' : '2008',
    'v2009' : '2009',
    'v2010' : '2010',
    'v2011' : '2011',
    'v2012' : '2012',
    'v2013' : '2013',
    'v2014' : '2014',
    'v2015' : '2015',
    'v2016' : '2016',
}

dangActs_mapping = {
    'v2003' : '2003',
    'v2004' : '2004',
    'v2005' : '2005',
    'v2006' : '2006',
    'v2007' : '2007',
    'v2008' : '2008',
    'v2009' : '2009',
    'v2010' : '2010',
    'v2011' : '2011',
    'v2012' : '2012',
    'v2013' : '2013',
    'v2014' : '2014',
    'v2015' : '2015',
    'v2016' : '2016',
}

drugs_mapping = {
    'v2003' : '2003',
    'v2004' : '2004',
    'v2005' : '2005',
    'v2006' : '2006',
    'v2007' : '2007',
    'v2008' : '2008',
    'v2009' : '2009',
    'v2010' : '2010',
    'v2011' : '2011',
    'v2012' : '2012',
    'v2013' : '2013',
    'v2014' : '2014',
    'v2015' : '2015',
    'v2016' : '2016',
}

fraud_mapping = {
    'v2003' : '2003',
    'v2004' : '2004',
    'v2005' : '2005',
    'v2006' : '2006',
    'v2007' : '2007',
    'v2008' : '2008',
    'v2009' : '2009',
    'v2010' : '2010',
    'v2011' : '2011',
    'v2012' : '2012',
    'v2013' : '2013',
    'v2014' : '2014',
    'v2015' : '2015',
    'v2016' : '2016',
}

govmnt_mapping = {
    'v2003' : '2003',
    'v2004' : '2004',
    'v2005' : '2005',
    'v2006' : '2006',
    'v2007' : '2007',
    'v2008' : '2008',
    'v2009' : '2009',
    'v2010' : '2010',
    'v2011' : '2011',
    'v2012' : '2012',
    'v2013' : '2013',
    'v2014' : '2014',
    'v2015' : '2015',
    'v2016' : '2016',
}

kidnap_mapping = {
    'v2003' : '2003',
    'v2004' : '2004',
    'v2005' : '2005',
    'v2006' : '2006',
    'v2007' : '2007',
    'v2008' : '2008',
    'v2009' : '2009',
    'v2010' : '2010',
    'v2011' : '2011',
    'v2012' : '2012',
    'v2013' : '2013',
    'v2014' : '2014',
    'v2015' : '2015',
    'v2016' : '2016',
}

property_mapping = {
    'v2003' : '2003',
    'v2004' : '2004',
    'v2005' : '2005',
    'v2006' : '2006',
    'v2007' : '2007',
    'v2008' : '2008',
    'v2009' : '2009',
    'v2010' : '2010',
    'v2011' : '2011',
    'v2012' : '2012',
    'v2013' : '2013',
    'v2014' : '2014',
    'v2015' : '2015',
    'v2016' : '2016',
}

robbery_mapping = {
    'v2003' : '2003',
    'v2004' : '2004',
    'v2005' : '2005',
    'v2006' : '2006',
    'v2007' : '2007',
    'v2008' : '2008',
    'v2009' : '2009',
    'v2010' : '2010',
    'v2011' : '2011',
    'v2012' : '2012',
    'v2013' : '2013',
    'v2014' : '2014',
    'v2015' : '2015',
    'v2016' : '2016',
}

social_mapping = {
    'v2003' : '2003',
    'v2004' : '2004',
    'v2005' : '2005',
    'v2006' : '2006',
    'v2007' : '2007',
    'v2008' : '2008',
    'v2009' : '2009',
    'v2010' : '2010',
    'v2011' : '2011',
    'v2012' : '2012',
    'v2013' : '2013',
    'v2014' : '2014',
    'v2015' : '2015',
    'v2016' : '2016',
}

theft_mapping = {
    'v2003' : '2003',
    'v2004' : '2004',
    'v2005' : '2005',
    'v2006' : '2006',
    'v2007' : '2007',
    'v2008' : '2008',
    'v2009' : '2009',
    'v2010' : '2010',
    'v2011' : '2011',
    'v2012' : '2012',
    'v2013' : '2013',
    'v2014' : '2014',
    'v2015' : '2015',
    'v2016' : '2016',
}

threats_mapping = {
    'v2003' : '2003',
    'v2004' : '2004',
    'v2005' : '2005',
    'v2006' : '2006',
    'v2007' : '2007',
    'v2008' : '2008',
    'v2009' : '2009',
    'v2010' : '2010',
    'v2011' : '2011',
    'v2012' : '2012',
    'v2013' : '2013',
    'v2014' : '2014',
    'v2015' : '2015',
    'v2016' : '2016',
}

weapons_mapping = {
    'v2003' : '2003',
    'v2004' : '2004',
    'v2005' : '2005',
    'v2006' : '2006',
    'v2007' : '2007',
    'v2008' : '2008',
    'v2009' : '2009',
    'v2010' : '2010',
    'v2011' : '2011',
    'v2012' : '2012',
    'v2013' : '2013',
    'v2014' : '2014',
    'v2015' : '2015',
    'v2016' : '2016',
}

stations_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Garda_Stations3.shp'),
)

stations_burg = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'burglary.json'),
)

stations_dang = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'dangActs.json'),
)

stations_drugs = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'drugs.json'),
)

stations_fraud = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'fraud.json'),
)

stations_govmnt = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'govmnt.json'),
)

stations_kidnap = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'kidnap.json'),
)

stations_property = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'property.json'),
)

stations_robbery = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'robbery.json'),
)

stations_social = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'social.json'),
)

stations_theft = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'theft.json'),
)

stations_threats = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'threats.json'),
)

stations_weapons = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'weapons.json'),
)

def run(verbose=True):
    lm = LayerMapping(
        Burglary, stations_burg, burglary_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)