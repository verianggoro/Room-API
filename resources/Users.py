from flask_restful import Resource, reqparse
from model.UserModel import UserModel, UserSchema

parser = reqparse.RequestParser()
parser.add_argument('username', required=True, help='Username Is Required')
parser.add_argument('password', required=True, help='Password Is Required')


class User(Resource):
    decorator = []

    def post(self):
        data = parser.parse_args()
        userName = data['username']
        password = data['password']

        login = UserModel.query.filter(UserModel.username == userName) \
            .filter(UserModel.password == password).first()

        loginSchema = UserSchema()
        result = loginSchema.dump(login).data
        if result:
            return {
                'status': 1,
                'message': 'Success',
                'data': result
            }
        else:
            return {
                'status': 0,
                'message': 'Failed',
                'data': ''
            }
