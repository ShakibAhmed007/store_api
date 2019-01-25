from models.user import user

User_List = [user(id=1,name='shakib',password = '12345'),
             user(id=2,name='shojon',password = '12345'),
             user(id=3,name='zahid',password = '12345')]


def verify(username , password):
    if not (username and password):
        return False
    User = user.find_user(username,password)
    return User



def identity(payload):
    user_id = payload['identity']
    return {'user_id':user_id}