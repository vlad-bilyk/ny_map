import json


def read_data(filename):
    '''
    Generator type function for reading data from file
    :param filename: str
    :return: dict
    '''
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            print(line)
            try:
                info = {
                    'station': line[3],
                    'date': line[6],
                    'time': line[7],
                    'entrances': int(line[9]),
                    'exits': int(line[10]),
                    'coords': [float(line[11]), float(line[12])]
                }
            except:
                continue
            yield info


def write_data(filename, data):
    '''
    Function for writing data into json file
    :param filename: str
    :param data: str
    :return: None
    '''
    with open(filename, 'w') as file:
        json.dump(data, file)


def to_json(outfile, infile, times=200):
    '''
    Function for converting txt data into json
    :param outfile: str
    :param infile: str
    :param times: int
        a limiter dedicating how many points will be added to json
    :return: None
    '''
    data_gen = read_data(outfile)

    DATA = {
        'info': []
    }

    for i in range(times):
        DATA['info'].append(next(data_gen))

    DATA['info'].sort(key=lambda x: x['date'])
    write_data(infile, DATA)
    print("data was converted")


def get_duration(outfile, times=200):
    '''
    Function for getting the total number of days
    :param outfile: str
    :param times: int
        a limiter dedicating how many points will be added to json
    :return: int
    '''
    data_gen = read_data(outfile)

    DATA = {
        'info': []
    }

    for i in range(times):
        DATA['info'].append(next(data_gen))

    FIRST_DAY = DATA['info'][0]['date'][3:5]
    LAST_DAY = DATA['info'][-1]['date'][3:5]
    DURATION = str(int(LAST_DAY) - int(FIRST_DAY))
    return DURATION


if __name__ == "__main__":
    to_json('../data/data.txt', '../data/newdata.json', 800)
