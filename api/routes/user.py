from flask import Blueprint
import uuid
from flask import request, jsonify
from werkzeug.security import generate_password_hash
from ..extensions.database import db
from ..models import User
from .login import token_required

user = Blueprint('user', __name__)


@user.route('/api/user/<nickname>', methods=['GET'])
@token_required
def get_single_user(current_user, nickname):
    user = User.query.filter_by(nickname=nickname).first()

    if not user:
        return jsonify({'message': 'No user found.'})
    user_data = {}
    user_data['nickname'] = user.name
    user_data['public_id'] = user.public_id
    user_data['rank'] = user.rank
    user_data['level'] = user.level
    user_data['trees'] = user.trees
    user_data['userXP'] = user.userXP
    user_data['userKM'] = user.userKM
    user_data['amountOfC02'] = user.amountOfC02

    return user_data


@user.route('/api/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({'message': 'No user found.'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted.'})


@user.route('/api/register', methods=['POST'])
def register_new_user():
    data = request.get_json()
    hashed_pass = generate_password_hash(data['password'], method='sha256')
    new_user = User(str(uuid.uuid4()), hashed_pass, data['nickname'])
    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        return jsonify({'message': 'User already exists!'}), 409
    return jsonify({'message': 'User created!'}), 201
