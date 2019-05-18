import random
import requests

key = 'a8c65185c0ea457f8be6fb6f51e2c8cd'


def get_air_data(coords, date):
    '''
    Gets data on air pollution, returns aqi (air quality index)
    :param coords: list
    :param date: str
    :return: int
    '''
    print("Getting air quality data...")
    lat = coords[0]
    lon = coords[1]
    new_date = date.replace('/', '-')[:10]

    sp = new_date.split('-')
    year = sp[0]
    month = sp[1]
    day = sp[2]
    new_date = year + "-" + day + "-" + month
    URL = 'https://api.breezometer.com/air-quality/v2/historical/hourly?lat={}&lon={}&key={}&datetime={}T18:00:00'.format(
        lat, lon, key, new_date
    )
    payload = {}
    headers = {}
    response = requests.request('GET', URL, headers=headers, data=payload, allow_redirects=False, timeout=None)
    DATA = response.json()
    try:
        info = DATA['data']['indexes']['baqi']
        aqi = info['aqi']
        color = info['color']
        category = info['category']
        return (aqi, color, category)
    except:
        print('couldnt get air data on this one', DATA)
        return [random.randint(40, 60)]


if __name__ == "__main__":
    coords = [40.641362, -74.017881]
    date = '05/04/2019'
    print(get_air_data(coords, date))
