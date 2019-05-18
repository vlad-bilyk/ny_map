from data import info, json_data
from map import folium_map


def main(day, limit=1000):
    '''
    Main function including all other sub-main functions
    :param day: str
    :param limit: int
    :return: None
    '''
    # loading data
    print('collecting info')
    info.get_info_with_last(day)
    print('info was collected')
    # converting data to json
    print('converting to json')
    json_data.to_json('../NY_MAP/data/data.txt', '../NY_MAP/data/newdata.json', limit)
    print('converted')
    # creating a map
    print('creating a map')
    folium_map.create_map()
    print('map was created')

if __name__ == "__main__":
    main('MON')