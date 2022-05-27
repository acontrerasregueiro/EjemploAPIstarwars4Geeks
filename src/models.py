from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=True)
    gender = db.Column(db.String(120), unique=False, nullable=True)
    hair_color = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<People %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
        }
        

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=True)
    terrain = db.Column(db.String(120), unique=False, nullable=True)
    climate = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<Planets %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "climate": self.climate,
        }


class Fav_people(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    rel_user = db.relationship(User)
    rel_people = db.relationship(People)

    def __repr__(self):
        return '<FavPeople %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id
        }

class Fav_planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    rel_user = db.relationship(User)
    rel_planet = db.relationship(Planets)

    def __repr__(self):
        return '<FavPlanets %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet.id
        }