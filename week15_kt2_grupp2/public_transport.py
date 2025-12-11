#from data_public_transport import
from abc import ABC, abstractmethod
class PublicTransport(object):
    transport_type = str
    def __init__(self, route_number, route_name, start_stop, end_stop, num_stops, distance_km, avg_speed_kmh, ticket_price, frequency_min, operates_nights,wheelchair_accessible,air_conditioned, bike_capacity, power_type):
        if not self.is_valid_speed(avg_speed_kmh):
            raise ValueError (f'Marsruudi {route_number} keskmine kiirus peab olema 10-50 km/h vahel! Saadud: {avg_speed_kmh}')
        if not self.is_valid_fare(ticket_price) >=0:
            raise ValueError (f'Marsruudi {route_number} piletihind peab olema positiivne! Saadud: {ticket_price}')

        #salvestan atribuudid
        self.route_number = route_number
        self.route_name = route_name
        self.start_stop = start_stop
        self.end_stop = end_stop
        self.num_stops = num_stops
        self.distance_km = distance_km
        self.avg_speed_kmh = avg_speed_kmh
        self.ticket_price = ticket_price
        self.frequency_min = frequency_min
        self.operates_nights = operates_nights
        self.wheelchair_accessible = wheelchair_accessible
        self.bike_capacity = bike_capacity
        self.power_type = power_type



    @staticmethod
    def is_valid_speed(avg_speed_kmh):
        if not isinstance (avg_speed_kmh, int, float):
            return False
        if isinstance(avg_speed_kmh, int, float) and 10 <= avg_speed_kmh <= 50:
            return True

        return False
    @staticmethod
    def is_valid_fare(ticket_price):
        if not isinstance (ticket_price, float):
            return False
        if isinstance(ticket_price, float) and ticket_price >= 0.0:
            return True

    @abstractmethod
    def calculate_trip_duration():
        pass

    @abstractmethod
    def calculate_ticket_price(distance_traveled_km):
        pass

    def get_route_info():
        return (f"Marsruut {route_number}: {start_stop} - {end_stop}")

