import http.client, urllib.parse, json
from kaartautomaat.logic.getCurrentstation import *
key = { 'Ocp-Apim-Subscription-Key': 'c3ff9bf4988c4021bd5bd2ebd5d8efef'}

def getDepartures(location = huidigStation()):
    try:
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
        for i in departuresList:
            info = {
                "tijd" : i['actualDateTime'],
                "bestemming" : i['direction'],
                "spoor" : i['plannedTrack'],
                "type" : i['product']['longCategoryName']
            }
            exportinfo.append(info)
        conn.close()
        return exportinfo
    except Exception as e:
        print("Fout: "+str(e.args))

getDepartures()