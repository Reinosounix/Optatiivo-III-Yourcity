from flask import Blueprint, request, jsonify
from project import db
from project.municipalities.models import Municipality
from project.municipalities.serializers import municipality_schema


municipality_blueprint = Blueprint('municipalities', __name__)


def save_municipality(municipality):
    db.session.add(municipality)
    db.session.commit()


@municipality_blueprint.route('/municipalities', methods=['POST'])
def create():
    municipality = municipality_schema.load(request.get_json())

    save_municipality(municipality)

    return municipality_schema.dump(municipality), 201


@municipality_blueprint.route('/municipalities/<id>', methods=['PUT'])
def update(id):
    municipality = Municipality.query.filter_by(id=id).first()

    if municipality is None:
        return 'Not found', 404

    municipality = municipality_schema.load(
        request.get_json(), instance=municipality)

    save_municipality(municipality)

    return municipality_schema.dump(municipality), 200


@municipality_blueprint.route('/municipalities/<id>', methods=['PATCH'])
def patch(id):
    municipality = Municipality.query.filter_by(id=id).first()
    municipality = municipality_schema.load(
        request.get_json(), instance=municipality, partial=True)

    save_municipality(municipality)

    return municipality_schema.dump(municipality), 200


@municipality_blueprint.route('/municipalities', methods=['GET'])
def list():
    municipalities = Municipality.query.all()

    return jsonify(municipality_schema.dump(municipalities, many=True)), 200
