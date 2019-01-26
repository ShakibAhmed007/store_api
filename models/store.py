from db import db

class store(db.Model):

    __tablename__ = 'store'
    id = db.Column(db.Integer , primary_key=True)
    store_name = db.Column(db.String)
    store_location = db.Column(db.String)



    def __init__(self,store_name,store_location):
        self.store_name = store_name
        self.store_location = store_location

    @classmethod
    def get_all_store(cls):
      Store_list = []
      all_store =  db.session.query(cls).all()
      for st in all_store:
       store_info = {'id':st.id,'name:':st.store_name,'location':st.store_location}
       Store_list.append(store_info)

      return Store_list




    @classmethod
    def insert_store_info(cls,store_name,store_location):
        Store1 = cls(store_name, store_location)

        db.session.add(Store1)
        db.session.commit()



    @classmethod
    def update_store_data(cls , id , name , location):
        Store1 = db.session.query(store).filter_by(id = id).first()
        Store1.store_name = name;
        Store1.store_location = location;

        db.session.commit()



    @classmethod
    def delete_store_data(cls ,id):
        Store1 = db.session.query(store).filter_by(id = id).first()

        db.session.delete(Store1)
        db.session.commit()


