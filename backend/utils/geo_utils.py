from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class GeoUtils:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="civic_issue_app")
    
    def get_address_from_coordinates(self, latitude, longitude):
        """Convert coordinates to address"""
        try:
            location = self.geolocator.reverse(f"{latitude}, {longitude}")
            return location.address if location else None
        except:
            return None
    
    def get_coordinates_from_address(self, address):
        """Convert address to coordinates"""
        try:
            location = self.geolocator.geocode(address)
            if location:
                return {
                    'latitude': location.latitude,
                    'longitude': location.longitude
                }
            return None
        except:
            return None
    
    @staticmethod
    def calculate_distance(coord1, coord2):
        """Calculate distance between two coordinates in kilometers"""
        return geodesic(coord1, coord2).kilometers
    
    @staticmethod
    def is_within_radius(center, point, radius_km):
        """Check if point is within radius of center"""
        distance = GeoUtils.calculate_distance(center, point)
        return distance <= radius_km
