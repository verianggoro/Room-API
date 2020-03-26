from model.RoomModel import RoomModel, RoomSchema
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()


class Room(Resource):
    decorator = []

    def get(self):
        roomQuery = RoomModel.query.all()
        roomSchema = RoomSchema(many=True)
        result = roomSchema.dump(roomQuery).data
        return {
            'rooms': result
        }
