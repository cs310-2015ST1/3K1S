__author__ = 'taeyeonkim90'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liquor.settings')
import django
django.setup()
from liquor_locator.models import LiquorStore
import csv
#import urllib2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(BASE_DIR, 'static')

def populate():
    #url = 'http://www.pssg.gov.bc.ca/lclb/docs-forms/web_lrs.csv'
    #response = urllib2.urlopen(url)
    response = os.path.join(STATIC_PATH, 'data.csv')
    
    with open(response, 'rb') as csvfile:

        storeinfo = csv.reader(csvfile, delimiter=',')
        next(storeinfo, None)
        for row in storeinfo:
            tmp = LiquorStore.objects.create()
            tmp.name = row[2]
            tmp.address = row[3]
            tmp.storetype = row[4]
            tmp.lat = row[5]
            tmp.lon = row[6]
            tmp.save()

# Start execution here!
if __name__ == '__main__':
    print "Starting LiquorStore population script..."
    print BASE_DIR
    print STATIC_PATH
    populate()