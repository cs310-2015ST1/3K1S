__author__ = 'ryan'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liquor.settings')
import django
django.setup()
from liquor_locator.models import LiquorStore
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(BASE_DIR, 'static')

def populate():
    #url = 'http://www.pssg.gov.bc.ca/lclb/docs-forms/web_lrs.csv'
    #response = urllib2.urlopen(url)
    response = os.path.join(STATIC_PATH, 'data_hours.csv')
    
    with open(response, 'rb') as csvfile:

        storeinfo = csv.reader(csvfile, delimiter=',')
        next(storeinfo, None)
        for i, row in enumerate(storeinfo):
            tmp = LiquorStore.objects.create()
            tmp.name = row[1]
            tmp.address = row[2]
            tmp.storetype = row[3]
            tmp.lat = row[4]
            tmp.lon = row[5]
            tmp.hours = row[6]
            tmp.save()


# Start execution here!
if __name__ == '__main__':
    print "Starting LiquorStore population script..."
    populate()