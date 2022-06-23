from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password= db.Column(db.Integer, unique=False, nullable=False)
    id_user = db.relationship('favorites', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.user_name
   
    def serialize(self):
        return {
            "id": self.id,
            "username": self.user_name,
            "email": self.email,
        }

class Favorites(Base):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'),nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'),nullable=True) 
    ship_id = db.Column(db.Integer, db.ForeignKey('ships.id'),nullable=True)

    def __repr__(self):
        return '<Favorites %r>' % self.user_id
   
    def serialize(self):
        return {
            "id": self.id,
            "username": self.user_id,
            "character": self.character_id,
            "planet": self.planet_id, 
            # Me interesaría que serializara el nombre en vez del id??
            "starship": self.ship_id,  
        }
         
class Character(Base):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    eye_color = db.Column(db.String(30), unique=False, nullable=False)
    hair_color = db.Column(db.String(30), unique=False, nullable=False)
    year_of_birth = db.Column(db.String(10), unique=False, nullable=False)
    gender = db.Column(db.String(10), unique=False, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    ships_id = db.Column(db.Integer, db.ForeignKey('ships.id'),nullable=False)
    favorite_character = db.relationship('favorites', backref='character', lazy=True)

    def __repr__(self):
        return '<Character %r>' % self.name
   
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye color": self.eye_color,
            "hair color": self.hair_color, 
            "birth": self.year_of_birth, 
            "gender": self.gender, 
            # Me interesaría que serializara el nombre en vez del id??
            # Puede ir sin espacio?
            "planet": self.planet_id,  
            "starship": self.ships_id  
        }


class Planet(Base):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    diameter = db.Column(db.Integer, unique=False, nullable=False)
    climate = db.Column(db.String(20), unique=False, nullable=True)
    terrain = db.Column(db.String(20), unique=False, nullable=True)
    characters = db.relationship('character', backref='planet', lazy=True)
    favorite_planet = db.relationship('favorites', backref='planet', lazy=True)

    def __repr__(self):
        return '<Planet %r>' % self.name
   
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population, 
            "diameter": self.diameter, 
            "climate": self.climate, 
            "terrain": self.terrain
        }    
    

class Ships(Base):
    __tablename__ = 'ships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    model = db.Column(db.String(30), unique=False, nullable=False)
    length = db.Column(db.Integer, unique=False, nullable=False)
    manufacturer = db.Column(db.String(100), unique=False, nullable=False)
    capacity = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Ships %r>' % self.name
   
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "length": self.length,
            "manufacturer":self.manufacturer,
            "capacity":self.capacity
        }    
          