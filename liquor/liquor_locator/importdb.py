import csv
import urllib2

url = 'http://www.pssg.gov.bc.ca/lclb/docs-forms/web_lrs.csv'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for row in cr:
    print row