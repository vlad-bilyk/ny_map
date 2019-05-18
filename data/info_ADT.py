import csv
import urllib.request
import urllib
import ssl
from data.get_new_file import get_last


class Info:
    """
        A class used to represent information

        ...

        Attributes
        ----------
        filename : str
            a string representing the filename from which information is taken
        day: str
            a string representing the day
        size : int
            the size of an Info object
        data_type : str
            a string representing the type of data current object contains
        source : str
            string representing source of the information
        data : list
            list containing data

        Methods
        -------
        get_data_type()
            Returns the data type attribute
        get_size()
            Returns the size attribute
        get_source()
            Returns the source attribute
        txt_read(filename)
            Reads data from a file or url, formating it and converting into lst
            Return a list of data
        """

    def __init__(self, filename=None, day='MON'):
        '''
        Initializing
        :param filename: str
        :param day: str
        '''
        self.day = day
        self.filename = filename
        self.size = 0
        self.data_type = None
        self.source = filename
        if filename is None:
            self.data = None
        elif filename.endswith('txt'):
            self.data = self.txt_read(filename)
            self.data_type = 'txt'
        elif filename.endswith('csv'):
            self.data = self.csv_read(filename)
            self.data_type = 'csv'

    def get_data_type(self):
        '''
        Return the data type
        :return: str
        '''
        return self.data_type

    def get_size(self):
        '''
        Returns the size of data
        :return: int
        '''
        return self.size

    def get_source(self):
        '''
        Return the name of data source
        :return: str
        '''
        return self.source

    def txt_read(self, filename, limit=2000):
        '''
        Reads data from txt file from url
        :param filename: str
        :param limit: int
        :return: list
        '''
        chosen_day = self.day
        k = 0
        days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        day_number = days.index(chosen_day)

        counter = 0
        day_counter = 0
        DATA = []
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(filename, context=context) as webpage:
            webpage.readline()
            for b in webpage:
                if k == limit:
                    break
                line = b.strip()
                line = line.decode("utf-8")
                curr_st = line.split(',')[3]
                curr_el = line.split(',')[2]
                curr_date = line.split(',')[6]
                # print(line)

                if counter > 0:
                    if curr_st != prev_st:
                        day_counter = -1
                        # print('new st: ', curr_st)

                if counter > 0:
                    if curr_date != prev_date:
                        # print('new day')
                        day_counter += 1
                        # print('day_counter: ', day_counter)

                if day_counter == day_number:
                    # print('adding')
                    # print("day counter: ", day_counter)
                    # print(curr_date)
                    DATA.append(line)
                    self.size += 1
                    k += 1
                    counter += 1
                    prev_date = curr_date
                    prev_st = curr_st
                    continue

                counter += 1
                prev_el = curr_el
                prev_st = curr_st
                prev_date = curr_date


        return DATA


    def csv_read(self, filename):
        '''
        Reads info from csv file
        :param filename: str
        :return: list
        '''
        DATA = []
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                newrow = []
                for el in row:
                    newrow.append(el.lower())
                self.size += 1
                DATA.append(newrow[3:6] + newrow[-2:])

        return DATA

    def write(self, filename):
        '''
        Writes data into file
        :param filename: str
        :return: None
        '''
        with open(filename, 'w') as file:
            for i in self.data:
                file.write(i + '\n')
            # file.write(self.data)
        print("data was written")


    def __add__(self, other):
        '''
        Adds csv and txt data, combining them together
        :param other: object
        :return: object
        '''
        txt_data = self.data if self.filename.endswith('txt') else other.data
        csv_data = self.data if self.filename.endswith('csv') else other.data
        DATA = []
        numbers = [str(i) for i in range(10)]
        for line in txt_data:
            line = line.lower().split(",")
            for s in csv_data:
                if s[0] in line:
                    if s[2] in line:
                        line.append(str(s[-2]))
                        line.append(str(s[-1]))
                        break
                    else:
                        if [i for i in line[3] if i in numbers] \
                                == [i for i in s[2] if i in numbers] \
                                and abs(len(line[3]) - len(s[2])) <= 4:

                            line.append(str(s[-2]))
                            line.append(str(s[-1]))
                            break
                        else:
                            pass
            line = ",".join(line)
            DATA.append(line)

        newInfo = Info()
        newInfo.size = self.get_size() + other.get_size()
        newInfo.data = DATA
        newInfo.data_type = 'combined {} and {}'.format(self.get_data_type(), other.get_data_type())
        newInfo.source = "{} data + {} data".format(self.get_data_type(), other.get_data_type())
        return newInfo

    def __str__(self):
        '''
        str method
        :return: str
        '''
        s = "Contains {} data\nSize: {} lines\nsource: {}".format(self.get_data_type(), self.get_size(), self.get_source())
        return s


if __name__ == "__main__":
    txt_data = Info("http://web.mta.info/developers/" + get_last()[0], 'MON')
    # txt_data = Info("http://web.mta.info/developers/" + get_last()[0], 'SUN')
    # txt_data = Info("http://web.mta.info/developers/" + get_last()[0], 'FRI')
    csv_data = Info("../data/Stations.csv")
    data = txt_data + csv_data
    data.write('data_test.txt')
