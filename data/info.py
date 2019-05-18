from data.info_ADT import Info
from data.get_new_file import get_last



def get_info_with_last(day):
    '''
    Get the latest data from url and csv file and write it into a file
    :return: None
    '''
    txt_data = Info("http://web.mta.info/developers/" + get_last()[0], day)
    csv_data = Info("../NY_MAP/data/Stations.csv")
    data = txt_data + csv_data
    data.write('../NY_MAP/data/data.txt')
