from kaartautomaat.logic.Apirequester import getStations

def getCode(station):
    # haalt lijst met stations op
    stations = getStations()
    # loopt door alle stations heen tot hij een station vind met de juiste naam
    for i in stations:
        for naam in i['namen'].values():
            # als station met de juiste naam gevonden word word deze gereturned
            if naam.lower() == station.lower():
                return i['code']
    # als het station niet gevonden kon worden word er een exception geraised
    raise Exception('Station {} kon niet gevonden worden'.format(station))
