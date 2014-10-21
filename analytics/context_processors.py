from localflavor.us.us_states import STATES_NORMALIZED
from analytics.models import Ads


def location(request):
    return {
        'location': request.location
    }


def filtered_ads(request):
    location = STATES_NORMALIZED['state']
    return {
      'filtered_ads': Ads.objects.filter(state=request.location).order_by('?')[0]
      # 'filtered_ads': Ads.objects.order_by('?')[0]
    }