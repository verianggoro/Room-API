from app import db, ma


class ListBookedModel(db.Model):
    __tablename__ = 'data_booking'
    __tableargs__ = {'extend_existing': True}


class ListBookedSchema(ma.ModelSchema):
    class Meta:
        model = ListBookedModel