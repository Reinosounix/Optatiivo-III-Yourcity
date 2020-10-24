from flask import Blueprint, request, jsonify
from project import db
from project.users.models import User
from project.users.serializers import user_schema


user_blueprint = Blueprint('users', __name__)


def save_user(user):
    db.session.add(user)
    db.session.commit()


@user_blueprint.route('/users', methods=['POST'])
def create():
    user = user_schema.load(request.get_json())

    save_user(user)

    return user_schema.dump(user), 201


@user_blueprint.route('/users/<id>', methods=['PUT'])
def update(id):
    user = User.query.filter_by(id=id).first()

    if user is None:
        return 'Not found', 404

    user = user_schema.load(request.get_json(), instance=user)

    save_user(user)

    return user_schema.dump(user), 200


@user_blueprint.route('/users/<id>', methods=['PATCH'])
def patch(id):
    user = User.query.filter_by(id=id).first()
    user = user_schema.load(request.get_json(), instance=user, partial=True)

    save_user(user)

    return user_schema.dump(user), 200


@user_blueprint.route('/users', methods=['GET'])
def list():
    users = User.query.all()

    return jsonify(user_schema.dump(users, many=True)), 200
