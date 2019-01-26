from models.user import user

def verify(username , password):
    if not (username and password):
        return False
    User = user.find_user(username,password)
    return User



def identity(payload):
    user_id = payload['identity']
    return {'user_id':user_id}