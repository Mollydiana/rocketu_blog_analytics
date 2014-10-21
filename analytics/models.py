from django.db import models


class Page(models.Model):
    url = models.URLField(unique=True)

    def __unicode__(self):
        return u"{}".format(self.url)


class Location(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=30)

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
    url = models.URLField()
    state = models.CharField(max_length=40)