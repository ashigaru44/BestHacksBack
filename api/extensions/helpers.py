from ..models import User

def get_users_public_id(username):
    user = User.query.filter_by(nickname=username).first()

    return user.public_id