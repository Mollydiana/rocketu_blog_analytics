from analytics.models import Ads


def location(request):
    return {
        'location': request.location
    }


def filtered_ads(request):
    return {
      'ad': Ads.objects.filter(state=)
    }