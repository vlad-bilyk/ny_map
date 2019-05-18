from map.unchanged import *


class Circle:
    """
        A class used to represent a circle on the map

        ...

        Attributes
        ----------
        coords : list
            a list containing point longitude and latitude
        entrances : int
            a number representing the amount of entrances on the current station
        exits : int
            a number representing the amount of exits on the current station

        Methods
        -------
        get_district()
            Returns the area of bronx
        abs_ofpeople()
            Returns the abs of difference between entrances and exits
        count_radius()
            Returns the radius of a circle.
        """
    def __init__(self, coords, entrances=0, exits=0):

        self.coords = coords
        self.entrances = entrances
        self.exits = exits
        # self.area = None

    def get_district(self):
        '''
        Return the area of a district
        :return: int
        '''
        if BRONX[0][0] <= self.coords[0] <= BRONX[1][0] and BRONX[0][1] <= self.coords[1] <= BRONX[1][1]:
            return BRONX_AREA
            # self.area = BRONX_AREA

        elif MANHATTAN[0][0] <= self.coords[0] <= MANHATTAN[1][0] and MANHATTAN[0][1] <= self.coords[1] <= MANHATTAN[1][1]:
            return MANHATTAN_AREA
            # self.area = MANHATTAN_AREA

        elif BROOKLYN[0][0] <= self.coords[0] <= BROOKLYN[1][0] and BROOKLYN[0][1] <= self.coords[1] <= BROOKLYN[1][1]:
            return BROOKLYN_AREA
            # self.area = BRONX_AREA

        elif QUEENS[0][0] <= self.coords[0] <= QUEENS[1][0] and QUEENS[0][1] <= self.coords[1] <= QUEENS[1][1]:
            return QUEENS_AREA
            # self.area = QUEENS_AREA
        else:
            return BRONX_AREA
            # self.area = BRONX_AREA

    def abs_ofpeople(self):
        '''
        Returns the abs of difference of entrances and exits
        :return: int
        '''
        return abs(self.entrances - self.exits)

    def count_radius(self):
        """
        Returns the radius of a circle
        :return: int
        """
        for_one_km = int(self.abs_ofpeople() // self.get_district())
        coef = 10 ** (-len(str(for_one_km)) + 1)
        return int(for_one_km * coef) * 10


if __name__ == "__main__":
    circ = Circle([40.759901, -73.984139], 604221196, 37111525)
    # print(circ.get_district())
    # print(circ.area)
    print('people: ', circ.abs_ofpeople())
    print('r: ', circ.count_radius())

    circ = Circle([40.759901, -73.984139], 1196, 27111525)
    # print(circ.get_district())
    # print(circ.area)
    print('people: ', circ.abs_ofpeople())
    print('r: ', circ.count_radius())
    # print(circ.radius)
