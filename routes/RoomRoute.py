from app import api
from resources.Room import Room
from resources.Users import User
from resources.ListBooked import ListBooked

api.add_resource(Room, '/rooms')
api.add_resource(User, '/rooms/login')
api.add_resource(ListBooked, '/rooms/list-booked')
