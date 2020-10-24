from marshmallow import fields
from project import ma
from project.users.models import User, Address


class UserSchema(ma.SQLAlchemyAutoSchema):
    addresses = fields.Nested(
        many=True, nested='AddressSchema', dump_only=True)

    class Meta:
        model = User
        load_instance = True
        load_only = ('password',)


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        load_instance = True


user_schema = UserSchema()
