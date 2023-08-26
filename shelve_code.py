import shelve
import datetime
from pytz import timezone


class ShelveHandler:
    """
    Class handles the loading and writing to shelve
    Shelve is a type of data storage
    """

    def load(self, db_name):
        """
        Args:
            db_name: name of the db to load

        If the day stored in the db doesnt match the current day, then write the new day to the db and delete the information stored in INFO
        if INFO does not yet exist (first time running) create an empty dictionary
        Returns: data corresponding to the INFO

        """
        s = shelve.open(db_name)
        day = datetime.datetime.now(timezone("Europe/London")).strftime("%d")
        try:
            data = s['INFO']
            if s['day'] != day:
                del s['INFO']
            s['day'] = day
        except KeyError:
            data = {}
            s['INFO'] = data
            s['day'] = day
        finally:
            s.close()
        return data

    def write(self, db_name, d):
        """
        Args:
            db_name: name of the db to open
            d: data to add (if not exists already)
        if the dealer and product are not already in the data
        if the instance is not in the data for the dealer and product
        then add it to the data and assign the dealers data to the new data
        Returns:

        """
        s = shelve.open(db_name)
        data = self.load(db_name)
        for i in d.keys():

            # do what you want with the data here
            x = i.split(' ')[0]
            y = i.split(' ')[1]
            id = i.split(' ')[2]
            x_y = x + ' ' + y
            # do what you want with the data here

            if x_y not in data:
                data[x_y] = [id]
            elif id not in data[x_y]:
                data[x_y].append(id)
        s['INFO'] = data
        s.close()
