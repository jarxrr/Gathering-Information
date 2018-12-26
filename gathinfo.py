#!/usr/bin/python

from googleplaces import GooglePlaces, types, lang
import csv
import time
import os
import sys
def gathinfo(lokacja,obiekt,plik='plik.csv',radius = 20000):
    google_places = GooglePlaces(os.environ['API_KEY'])

    query_result = google_places.nearby_search(
            location=lokacja, keyword=obiekt,radius=radius)

    if query_result.has_attributions:
        print (query_result.html_attributions)

    with open(plik, mode='w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='|',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            while True:
                for place in query_result.places:
                    # Returned places from a query are place summaries.
                    place.get_details()
                    spamwriter.writerow([place.geo_location,place.name,place.place_id,place.types,place.vicinity,
                                         place.rating,place.formatted_address,place.local_phone_number,
                                         place.international_phone_number,place.website,place.url])
                if query_result.has_next_page_token :
                    time.sleep(0.1) 
                    query_result = google_places.nearby_search(location=lokacja,
                                                               keyword=obiekt,pagetoken=query_result.next_page_token)
                else:
                    break
    return

if __name__ == "__main__":
    a = (sys.argv[1])
    b = (sys.argv[2])
    if len(sys.argv) == 3:
        gathinfo(lokacja=a, obiekt=b,plik = a+'_'+b+'.csv')
    elif len(sys.argv) == 4:
        gathinfo(lokacja=a, obiekt=b,plik = (sys.argv[3]))
    else:
        gathinfo(lokacja=a, obiekt=b,plik = (sys.argv[3]),radius=int(sys.argv[4]))
    
   
