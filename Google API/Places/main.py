
# 
# https://stackoverflow.com/a/47912816/1832058
# 

import googlemaps

API_KEY = '<YOUR-API-KEY>'

gmaps = googlemaps.Client(key=API_KEY)

results = gmaps.places('Rugby Club, London')

for key in item.keys():
    print('key:', key)

print('-----')

for item in results['results']:
    print('name:', item['name'])
    print('lat:', item['geometry']['location']['lat'])
    print('lng:', item['geometry']['location']['lng'])
    print('location:', item['geometry']['location'])
    print('---')
    
print('-----')
    
#for item in results['results'][:1]:
#    for key, value in item.items():
#        print(key, ':', value)

    
