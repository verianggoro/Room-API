from model.ListBookedModel import ListBookedModel, ListBookedSchema
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()


class ListBooked(Resource):
    decorator = []

    def get(self):
        bookedQuery = ListBookedModel.query.all()
        bookedSchema = ListBookedSchema(many=True)
        result = bookedSchema.dump(bookedQuery).data
        return {
            'data': result
        }
