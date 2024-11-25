from opencage.geocoder import OpenCageGeocode

key = '05db6601914844ff8561da7f3f07c6ab'
geocoder = OpenCageGeocode(key)

query = u'Bosutska ulica 10, Trnje, Zagreb, Croatia'

# no need to URI encode query, module does that for you
results = geocoder.geocode(query)

print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'],
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))
# 45.797095;15.982453;hr;Europe/Belgrade