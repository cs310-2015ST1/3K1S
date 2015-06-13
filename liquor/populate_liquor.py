__author__ = 'taeyeonkim90'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liquor.settings')

import django
django.setup()

from liquor_locator.models import LiquorStore


def populate():
    # address is made by connecting column 1 and 3 from web_lrs.csv
    add_store("ABBOTSFORD,117 - 2070 SUMAS WAY", "49.039579,-122.270360", "BC Liquor Store", "ABBOTSFORD VILLAGE GLS 189")

    # this one doesn't have name. add_store() has default name NA set
    add_store("ABBOTSFORD,104 1520 MCCALLUM ROAD", "49.030667,-122.292672", "Proposed Store Location")
    add_store("CAMPBELL RIVER,2207B GLENMORE RD", "49.869879,-125.128688", "Private Liquor Store", "OYSTER RIVER LICENSED LIQUOR STORE")


def add_store(address, latlon, storetype, name="NA"):
    s = LiquorStore.objects.get_or_create(name=name, address=address, latlon=latlon, storetype=storetype)
    return s

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()