from flask import Response, request, jsonify
from api import app, db
from api.models.tables import User, UserSchema
import pprint


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route("/user", methods=["POST"])
def add_user():
    try:
        if (request.json['username'] == '') or (request.json['email'] == ''):
            return jsonify({'Msg': 'VALUE(s) not found in JSON sent.'}), 400

        new_user = User(request.json['username'], request.json['email'])
        db.session.add(new_user)
        db.session.commit()

        return user_schema.jsonify(new_user), 201
    except KeyError:
        return jsonify({'Error': 'JSON sent is not valid !'}), 400
    except Exception as e:
        pprint(e)
        return jsonify({'Error': 'Internal Error'}), 500


@app.route("/user", methods=["GET"])
def get_user():
    try:
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result.data)
    except Exception as e:
        pprint(e)
        return jsonify({'Error': 'Internal error'}), 500


@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({'Msg': 'User not found.'}), 404
        else:
            return user_schema.jsonify(user)
    except Exception as e:
        pprint(e)
        return jsonify({'Error': 'Internal error'}), 500


@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    try:
        if (request.json['username'] == '') or (request.json['email'] == ''):
            return jsonify({'Msg': 'VALUE(s) not found in JSON sent.'}), 400

        user = User.query.get(id)
        user.email = request.json['email']
        user.username = request.json['username']
        db.session.commit()

        return user_schema.jsonify(user)
    except KeyError:
        return jsonify({'Error': 'JSON sent is not valid !'}), 400
    except Exception as e:
        pprint(e)
        return jsonify({'Error': 'Internal error'}), 500


@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    try:
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return user_schema.jsonify(user)
    except Exception as e:
        pprint(e)
        return jsonify({'Error': 'Internal error'}), 500
