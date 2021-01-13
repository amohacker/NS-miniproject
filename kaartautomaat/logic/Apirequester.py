import http.client, urllib.parse, json
from kaartautomaat.logic.getCurrentstation import *
key = { 'Ocp-Apim-Subscription-Key': 'c3ff9bf4988c4021bd5bd2ebd5d8efef'}

def getDepartures(location = huidigStation()):
    try:
        # haalt de reisinformatie op vanuit de api
        params = urllib.parse.urlencode({
            'maxJourneys': '20',
            'station': location
        })
        conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
        conn.request("GET", "/reisinformatie-api/api/v2/departures?" + params, headers=key)

        response = conn.getresponse()
        responsetext = response.read()
        data = json.loads(responsetext)

        payloadObject = data['payload']
        departuresList = payloadObject['departures']

        exportinfo = []
        print('Cancelled:')
        for i in departuresList:
            info = {
                "tijd" : i['actualDateTime'],
                "bestemming" : i['direction'],
                "spoor" : i['plannedTrack'],
                "type" : i['product']['longCategoryName']
            }
            if i['cancelled']==True:
                print(info)
            if i['cancelled'] == False:
                exportinfo.append(info)

        conn.close()
        return exportinfo
    except Exception as e:
        print("Fout: "+str(e.args))

def getStations():
    try:
        # haalt lijst met stations op via de api
        conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
        conn.request("GET", "/reisinformatie-api/api/v2/stations?", headers=key)

        response = conn.getresponse()
        responsetext = response.read()
        data = json.loads(responsetext)
        # haalt het payloadobject uit de json en slaat het op in een lijst
        payloadObject = data['payload']
        exportinfo = []
        # haalt de nuttige informatie uit de lijst en stop het in een nieuwe lijst
        for i in payloadObject:
            namen = i['namen']
            info = {
                "code": i['code'],
                "namen": {
                    "lang": namen['lang'],
                    "middel": namen['middel'],
                    "kort": namen['kort']
                }
            }
            exportinfo.append(info)
        conn.close()
        return exportinfo
    except Exception as e:
        print("Fout: " + str(e.args))

# getDepartures()
# getStations()