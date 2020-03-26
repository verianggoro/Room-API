from app import db, ma


class UserModel(db.Model):
    __tablename__ = 'users'
    __tableargs__ = {'extend_existing': True}


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
