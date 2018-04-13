from django.contrib.gis.db import models

# Create your models here.

class GardaStations(models.Model):
    fid = models.CharField(max_length=80)
    name = models.CharField(max_length=80);
    blank = models.CharField(max_length=80);
    Sun = models.CharField(max_length=80);
    Address = models.CharField(max_length=80);
    Longitude = models.CharField(max_length=80);
    Latitude = models.CharField(max_length=80);
    County = models.CharField(max_length=80);
    Phone = models.CharField(max_length=80);
    StationID = models.CharField(max_length=80);
    Station = models.CharField(max_length=80);
    Mon_Fri = models.CharField(max_length=80);
    Sat = models.CharField(max_length=80);

    point = models.PointField();

    def __str__(self):
        return self.name

class Burglary(models.Model):
    v2003 = models.CharField(max_length=4);
    v2004 = models.CharField(max_length=4);
    v2005 = models.CharField(max_length=4);
    v2006 = models.CharField(max_length=4);
    v2007 = models.CharField(max_length=4);
    v2008 = models.CharField(max_length=4);
    v2009 = models.CharField(max_length=4);
    v2010 = models.CharField(max_length=4);
    v2011 = models.CharField(max_length=4);
    v2012 = models.CharField(max_length=4);
    v2013 = models.CharField(max_length=4);
    v2014 = models.CharField(max_length=4);
    v2015 = models.CharField(max_length=4);
    v2016 = models.CharField(max_length=4);
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name


class DangActs(models.Model):
    v2003 = models.CharField(max_length=4);
    v2004 = models.CharField(max_length=4);
    v2005 = models.CharField(max_length=4);
    v2006 = models.CharField(max_length=4);
    v2007 = models.CharField(max_length=4);
    v2008 = models.CharField(max_length=4);
    v2009 = models.CharField(max_length=4);
    v2010 = models.CharField(max_length=4);
    v2011 = models.CharField(max_length=4);
    v2012 = models.CharField(max_length=4);
    v2013 = models.CharField(max_length=4);
    v2014 = models.CharField(max_length=4);
    v2015 = models.CharField(max_length=4);
    v2016 = models.CharField(max_length=4);
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name


class Drugs(models.Model):
    v2003 = models.CharField(max_length=4);
    v2004 = models.CharField(max_length=4);
    v2005 = models.CharField(max_length=4);
    v2006 = models.CharField(max_length=4);
    v2007 = models.CharField(max_length=4);
    v2008 = models.CharField(max_length=4);
    v2009 = models.CharField(max_length=4);
    v2010 = models.CharField(max_length=4);
    v2011 = models.CharField(max_length=4);
    v2012 = models.CharField(max_length=4);
    v2013 = models.CharField(max_length=4);
    v2014 = models.CharField(max_length=4);
    v2015 = models.CharField(max_length=4);
    v2016 = models.CharField(max_length=4);
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name


class Fraud(models.Model):
    v2003 = models.CharField(max_length=4);
    v2004 = models.CharField(max_length=4);
    v2005 = models.CharField(max_length=4);
    v2006 = models.CharField(max_length=4);
    v2007 = models.CharField(max_length=4);
    v2008 = models.CharField(max_length=4);
    v2009 = models.CharField(max_length=4);
    v2010 = models.CharField(max_length=4);
    v2011 = models.CharField(max_length=4);
    v2012 = models.CharField(max_length=4);
    v2013 = models.CharField(max_length=4);
    v2014 = models.CharField(max_length=4);
    v2015 = models.CharField(max_length=4);
    v2016 = models.CharField(max_length=4);
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name


class Govmnt(models.Model):
    v2003 = models.CharField(max_length=4);
    v2004 = models.CharField(max_length=4);
    v2005 = models.CharField(max_length=4);
    v2006 = models.CharField(max_length=4);
    v2007 = models.CharField(max_length=4);
    v2008 = models.CharField(max_length=4);
    v2009 = models.CharField(max_length=4);
    v2010 = models.CharField(max_length=4);
    v2011 = models.CharField(max_length=4);
    v2012 = models.CharField(max_length=4);
    v2013 = models.CharField(max_length=4);
    v2014 = models.CharField(max_length=4);
    v2015 = models.CharField(max_length=4);
    v2016 = models.CharField(max_length=4);
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name


class Kidnap(models.Model):
    v2003 = models.CharField(max_length=4);
    v2004 = models.CharField(max_length=4);
    v2005 = models.CharField(max_length=4);
    v2006 = models.CharField(max_length=4);
    v2007 = models.CharField(max_length=4);
    v2008 = models.CharField(max_length=4);
    v2009 = models.CharField(max_length=4);
    v2010 = models.CharField(max_length=4);
    v2011 = models.CharField(max_length=4);
    v2012 = models.CharField(max_length=4);
    v2013 = models.CharField(max_length=4);
    v2014 = models.CharField(max_length=4);
    v2015 = models.CharField(max_length=4);
    v2016 = models.CharField(max_length=4);
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name


class Property(models.Model):
    v2003 = models.CharField(max_length=4);
    v2004 = models.CharField(max_length=4);
    v2005 = models.CharField(max_length=4);
    v2006 = models.CharField(max_length=4);
    v2007 = models.CharField(max_length=4);
    v2008 = models.CharField(max_length=4);
    v2009 = models.CharField(max_length=4);
    v2010 = models.CharField(max_length=4);
    v2011 = models.CharField(max_length=4);
    v2012 = models.CharField(max_length=4);
    v2013 = models.CharField(max_length=4);
    v2014 = models.CharField(max_length=4);
    v2015 = models.CharField(max_length=4);
    v2016 = models.CharField(max_length=4);
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name


class Robbery(models.Model):
    v2003 = models.CharField(max_length=4);
    v2004 = models.CharField(max_length=4);
    v2005 = models.CharField(max_length=4);
    v2006 = models.CharField(max_length=4);
    v2007 = models.CharField(max_length=4);
    v2008 = models.CharField(max_length=4);
    v2009 = models.CharField(max_length=4);
    v2010 = models.CharField(max_length=4);
    v2011 = models.CharField(max_length=4);
    v2012 = models.CharField(max_length=4);
    v2013 = models.CharField(max_length=4);
    v2014 = models.CharField(max_length=4);
    v2015 = models.CharField(max_length=4);
    v2016 = models.CharField(max_length=4);
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name


class Social(models.Model):
    v2003 = models.CharField(max_length=4);
    v2004 = models.CharField(max_length=4);
    v2005 = models.CharField(max_length=4);
    v2006 = models.CharField(max_length=4);
    v2007 = models.CharField(max_length=4);
    v2008 = models.CharField(max_length=4);
    v2009 = models.CharField(max_length=4);
    v2010 = models.CharField(max_length=4);
    v2011 = models.CharField(max_length=4);
    v2012 = models.CharField(max_length=4);
    v2013 = models.CharField(max_length=4);
    v2014 = models.CharField(max_length=4);
    v2015 = models.CharField(max_length=4);
    v2016 = models.CharField(max_length=4);
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name


class Theft(models.Model):
    v2003 = models.CharField(max_length=4);
    v2004 = models.CharField(max_length=4);
    v2005 = models.CharField(max_length=4);
    v2006 = models.CharField(max_length=4);
    v2007 = models.CharField(max_length=4);
    v2008 = models.CharField(max_length=4);
    v2009 = models.CharField(max_length=4);
    v2010 = models.CharField(max_length=4);
    v2011 = models.CharField(max_length=4);
    v2012 = models.CharField(max_length=4);
    v2013 = models.CharField(max_length=4);
    v2014 = models.CharField(max_length=4);
    v2015 = models.CharField(max_length=4);
    v2016 = models.CharField(max_length=4);
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name


class Threats(models.Model):
    v2003 = models.CharField(max_length=4);
    v2004 = models.CharField(max_length=4);
    v2005 = models.CharField(max_length=4);
    v2006 = models.CharField(max_length=4);
    v2007 = models.CharField(max_length=4);
    v2008 = models.CharField(max_length=4);
    v2009 = models.CharField(max_length=4);
    v2010 = models.CharField(max_length=4);
    v2011 = models.CharField(max_length=4);
    v2012 = models.CharField(max_length=4);
    v2013 = models.CharField(max_length=4);
    v2014 = models.CharField(max_length=4);
    v2015 = models.CharField(max_length=4);
    v2016 = models.CharField(max_length=4);
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name


class Weapons(models.Model):
    v2003 = models.CharField(max_length=4);
    v2004 = models.CharField(max_length=4);
    v2005 = models.CharField(max_length=4);
    v2006 = models.CharField(max_length=4);
    v2007 = models.CharField(max_length=4);
    v2008 = models.CharField(max_length=4);
    v2009 = models.CharField(max_length=4);
    v2010 = models.CharField(max_length=4);
    v2011 = models.CharField(max_length=4);
    v2012 = models.CharField(max_length=4);
    v2013 = models.CharField(max_length=4);
    v2014 = models.CharField(max_length=4);
    v2015 = models.CharField(max_length=4);
    v2016 = models.CharField(max_length=4);
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name