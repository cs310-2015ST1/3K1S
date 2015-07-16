import os
import django
import csv
import hashlib

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liquor.settings')
django.setup()

from liquor_locator.models import LiquorStore


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(BASE_DIR, 'static')

def populate():
    dataFeed = os.path.join(STATIC_PATH, 'data_hours_phone.csv')
    LiquorStore.objects.all().delete()
    with open(dataFeed, 'rb') as csvfile:
        storeinfo = csv.reader(csvfile, delimiter=',')
        next(storeinfo, None)
        for i, row in enumerate(storeinfo):
            store = LiquorStore.objects.create()
            store.name = row[1]
            store.address = row[2]
            store.storetype = row[3]
            store.lat = row[4]
            store.lon = row[5]
            store.hours = row[6]
            store.phone = row[7]

            # String concat & hash the string -> unique store ID
            stringToHash = row[1] + row[2] + row[3] + row[4] + row[5] + row[6] + row[7]
            md5Hash = hashlib.md5(stringToHash)
            print(md5Hash)
            store.storeHash = md5Hash.hexdigest()

            store.save()

# Start execution here!
if __name__ == '__main__':
    print "Starting LiquorStore population script..."
    populate()