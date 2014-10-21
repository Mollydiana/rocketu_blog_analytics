from django.db import models
from localflavor.us.models import USStateField
# from django.contrib.localflavor.us.us_states import US_STATES


class Page(models.Model):
    url = models.URLField(unique=True)

    def __unicode__(self):
        return u"{}".format(self.url)


class Location(models.Model):
    city = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    region = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        unique_together = (("city", "country", "region"),)

    def __unicode__(self):
        return u"{}".format(self.region)


class View(models.Model):
    ip_address = models.CharField(max_length=40, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, related_name="views", blank=True, null=True)
    page = models.ForeignKey(Page)
    latitude = models.FloatField(max_length=30, null=True)
    longitude = models.FloatField(max_length=30, null=True)

    def __unicode__(self):
        return u"{}".format(self.page, self.location, self.date_time)


class Ads(models.Model):
    img = models.ImageField(upload_to='adpics', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    state = USStateField(null=True, blank=True)

