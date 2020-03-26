from app import db, ma


class RoomModel(db.Model):
    __tablename__ = 'room'
    __tableargs__ = {'extend_existing': True}


class RoomSchema(ma.ModelSchema):
    class Meta:
        model = RoomModel
