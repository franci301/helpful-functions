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

        If the day stored in the db doesnt match the current day, then write the new day to the db and delete the information stored in dealers
        if dealers does not yet exist (first time running) create an empty dictionary
        Returns: data corresponding to the dealers

        """
        s = shelve.open(db_name)
        day = datetime.datetime.now(timezone("Europe/London")).strftime("%d")
        try:
            data = s['dealers']
            if s['day'] != day:
                del s['dealers']
            s['day'] = day
        except KeyError:
            data = {}
            s['dealers'] = data
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
            dealer = i.split(' ')[0]
            product = i.split(' ')[1]
            instance = i.split(' ')[2]
            dealer_prod = dealer + ' ' + product
            if dealer_prod not in data:
                data[dealer_prod] = [instance]
            elif instance not in data[dealer_prod]:
                data[dealer_prod].append(instance)
        s['dealers'] = data
        s.close()

