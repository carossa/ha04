"""
4. Hausaufgabe: Datenstrukturen

@author: Gruppe 10
"""


from numpy import sin, cos, arccos, pi

# ------------Small Datenbank------------ #
# -------------Airport Infos------------- #
airport_data = {'Berlin': {'lat': 52.365, 'lon': 13.51, 'ziel': ['Marrakesch', 'Montreal']},
                'Marrakesch': {'lat': 31.6, 'lon': -8.025, 'ziel': ['Berlin', 'Lima', 'Montreal']},
                'Montreal': {'lat': 45.67, 'lon': -74.04, 'ziel': ['Berlin', 'Marrakesch', 'Lima', 'Ulaanbaatar']},
                'Lima': {'lat': -12.02, 'lon': -77.11, 'ziel': ['Marrakesch', 'Montreal']},
                'Ulaanbaatar': {'lat': 47.85, 'lon': 106.76, 'ziel': ['Montreal']}
                }

start_airports = list(airport_data.keys())


# ---------Distance Calculation--------- #
# -----------Parameter in rad----------- #
def distance(lat1, lon1, lat2, lon2):
    orthodrome = arccos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(abs(lon2 - lon1)))  # Great Circle
    earth_radius = 6371  # in kilometer
    dist = earth_radius * orthodrome
    return dist


# -------------Input & Output----------- #
print('Servus!\nDieses Programm berechnet Flugdistanzen.\nBei welchem Flughafen wollen Sie Starten:', end=' ')

for i in start_airports:
    print(i, end=' ')

start_point = input()

if start_point not in start_airports:
    raise Exception('Fehler: eingegebener Flughafen existiert nicht oder wird vom Startflughafen nicht angeflogen!')

print('Zielflughaefen:', end=' ')

destinations = airport_data[start_point]['ziel']

for i in destinations:
    print(i, end=' ')

end_point = input()

if end_point not in destinations:
    raise Exception('Fehler: inkorrekte Eingabe!')

lt1 = (pi/180) * airport_data[start_point]['lat']  # function "distance() parameter: lat1 in rad
ln1 = (pi/180) * airport_data[start_point]['lon']  # function "distance() parameter: lon1 in rad
lt2 = (pi/180) * airport_data[end_point]['lat']  # function "distance() parameter: lat2 in rad
ln2 = (pi/180) * airport_data[end_point]['lon']  # function "distance() parameter: lon2 in rad

print(f'Distanz (in km): {round(distance(lt1, ln1, lt2, ln2))}\nProgramm beendet sich...')
