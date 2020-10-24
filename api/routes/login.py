from flask import Blueprint
from flask import request, jsonify, make_response
from ..models import User
from werkzeug.security import check_password_hash
from ..config import KEY
import jwt
import datetime
from functools import wraps

login = Blueprint('login', __name__)
blacklist = set()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401
        if token in blacklist:
            return jsonify({'message' : 'Token is expired!'}), 401
        try:
            data = jwt.decode(token, KEY, algorithms='HS256')
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)

    return decorated


@login.route('/api/login')
def log_in():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify.', 401)
    user = User.query.filter_by(nickname=auth.username).first()
    if not user:
        return make_response('Could not verify.', 401)
    if check_password_hash(user.password, auth.password):
        token = generate_token(user)

        return jsonify({'username': auth.username, 'token' : token.decode('UTF-8')})
    
    return make_response('Could not verify.', 401) 


@login.route('/api/refresh')
@token_required
def refresh_token(current_user):
    new_token = generate_token(current_user)
    # blacklist old token (switch to redis db soon)
    blacklist.add(request.headers['x-access-token'])
    # print(jwt.decode(request.headers['x-access-token'], KEY, algorithms='HS256'))
    return jsonify({'token' : new_token.decode('UTF-8')})



def generate_token(user):
    token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=6)}, KEY, algorithm='HS256')
    return token