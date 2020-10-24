from marshmallow import fields
from project import ma
from project.municipalities.models import Municipality


class MunicipalitySchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Municipality
        load_instance = True
        load_only = ('password',)


municipality_schema = MunicipalitySchema()
