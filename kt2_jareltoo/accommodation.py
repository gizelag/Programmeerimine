from abc import ABC, abstractmethod
class Accommodation():
    accommodation_type = str
    def __init__(self, name (str),address (str), city (str),base_price (float), rating (float),capacity (int),has_wifi (bool),has_parking (bool),has_breakfast (bool),check_in_time (str),check_out_time (str),min_nights):

        self.name = name
        self.address = address
        self.city = city
        self.base_price = base_price
        self.rating = rating
        self.capacity = capacity
        self.has_wifi = has_wifi
        self.has_parking = has_parking
        self.has_breakfast = has_breakfast
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        self.min_nights = min_nights

@staticmethod
    def is_valid_time():
        if not isinstance(is_valid_time, int):
            raise ValueError print (f'Majutuskoha {name} sisseregistreerimise/väljaregistreerimise aeg peab olema formaadis HH:MM! Saadud: {time}')


    @staticmethod
    def is_valid_rating(rating):
        if not isinstance (rating, float):
            raise ValueError
        if isinstance(rating, float) and 0.0 <= rating <= 5.0:
            return True