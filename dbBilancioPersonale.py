from app import db
from app.models.users import User
# from app.settings.settings import 


db.drop_all()
db.create_all()

admin = User(username='admin',email='admin@example.com')
guest = User(username='guest',email='guest@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()

