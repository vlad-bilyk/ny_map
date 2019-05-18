import json
import sys
sys.path.append("..")
from map.radius import Circle


def load_data(filename):
    '''
    Loading data from file into dct
    :param filename: str
    :return: dict
    '''
    with open(filename, 'r') as f:
        JSON_DATA = json.load(f)
        return JSON_DATA['info']


def create_points(filename):
    '''
    Creating points with station coordinates and other data that will be shown on the map
    :param filename: str
    :return: dict
    '''

    DATA = load_data(filename)

    points = []
    for info in DATA:

        # 1: "05/12/2019"
        # 2: 2019-12-05T16:00:00


        date = info['date'].split('/')
        year = date[2]
        month = date[0]
        day = date[1]
        date = year + '-' + month + '-' + day

        dct = {
            'station': info['station'],
            'time': date + "T" + info['time'],
            'popup': 'Station: {}'.format(info['station']),
            'coordinates': [info['coords'][1], info['coords'][0]],
            'entrances': info['entrances'],
            'exits': info['exits']
        }
        # print(dct)
        points.append(dct)


    features = []
    COORDINATES = []

    for point in points:
        stat = point['station']
        time = point['time']
        # print(time)
        coords = point['coordinates']

        if coords not in COORDINATES:
            COORDINATES.append(coords)

        entr = point['entrances']
        exits = point['exits']
        circle = Circle(coords, entr, exits)
        radius = circle.count_radius()
        popup = "Station: {}<br> Entrances: {}".format(stat, abs(entr - exits))
        color = 'red'
        if radius > 50:
            color = '#07eb96'  # green
        elif radius < 30:
            color = '#0abde3'  # blue
        elif radius <= 50:
            color = '#f04822'  # orange
        dct = {
                'type': 'Feature',
                'geometry': {
                    'type': 'MultiPoint',
                    'coordinates': [coords],
                },
                'properties': {
                    'times': [time],
                    'popup': popup,
                    'icon': 'circle',
                    'iconstyle': {
                        'fillColor': color,
                        'fillOpacity': 0.15,
                        'stroke': 'false',
                        'radius': radius
                        }
                }
            }

        features.append(dct)

    DEF_TIME = time

    def change_date(given):
        date = given.split('/')
        year = date[2]
        month = date[0]
        day = date[1]
        date = year + '-' + month + '-' + day
        return date

    features.append(
        {
            'type': 'Feature',
            'geometry': {
                'type': 'LineString',
                'coordinates': [
                    info['coords'] for info in DATA
                ],
            },
            'properties': {
                'popup': 'Current address',
                'times': sorted(set([change_date(info['date']) + "T" + info['time'] for info in DATA])),
                'icon': 'circle',
                'iconstyle': {
                    'fillColor': 'green',
                    'fillOpacity': 0.6,
                    'stroke': 'false',
                    'radius': 13
                },
                'style': {'weight': 0},
                'id': 'man'
            }
        }
    )

    result = {
        'features': features,
        'coordinates': COORDINATES,
        'set-time': DEF_TIME
    }
    return result
