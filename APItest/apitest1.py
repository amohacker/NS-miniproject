import http.client, urllib.parse, json

key = { 'Ocp-Apim-Subscription-Key': 'c3ff9bf4988c4021bd5bd2ebd5d8efef'}
params = urllib.parse.urlencode({
    'maxJourneys': '20',
    'station': 'Ut'
})

try:
    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request("GET", "/reisinformatie-api/api/v2/departures?"+params, headers=key)

    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)

    print(data)
    conn.close()
except Exception as e:
    print("Fout: {} {}".format(e.errno, e.strerror))

##https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/departures?station=UT&lang=nl&maxJourneys=20