from analytics.models import Ads


def location(request):
    return {
        'location': request.location
    }


def filtered_ads(request):
    return {
      'filtered_ads': Ads.objects.order_by('?')[0]
    }