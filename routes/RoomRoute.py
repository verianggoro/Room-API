from app import api
from resources.Room import Room
from resources.Users import User

api.add_resource(Room, '/rooms')
api.add_resource(User, '/rooms/login')
