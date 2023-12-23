import random

from django.contrib.gis.geoip2 import GeoIP2
from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def my_first_view(request: HttpRequest):
    g = GeoIP2()
    country = g.city("google.com")

    context = {
        "random_number": random.randint(0, 1024),
        "test": country
        # "meta_data": request.META["REMOTE_ADDR"]

    }
    return render(request=request, template_name='index.html', context=context)
