# models.py

from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy()

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    burgerName = db.Column(db.String(50), nullable=False)
    tomato = db.Column(db.Boolean, nullable=False, default=False)
    lettuce = db.Column(db.Boolean, nullable=False, default=False)
    onion = db.Column(db.Boolean, nullable=False, default=False)
    cheese = db.Column(db.Boolean, nullable=False, default=False)
    bun = db.Column(db.Boolean, nullable=False, default=False)
    meat = db.Column(db.Boolean, nullable=False, default=False)
    bacon = db.Column(db.Boolean, nullable=False, default=False)
    mockMeat = db.Column(db.Boolean, nullable=False, default=False)
    cucumber = db.Column(db.Boolean, nullable=False, default=False)
    chicken = db.Column(db.Boolean, nullable=False, default=False)
    jalapeno = db.Column(db.Boolean, nullable=False, default=False)


    def to_dict(self):
        return {
            'id': self.id,
            'burgerName': self.burgerName,
            'tomato': self.tomato,
            'lettuce': self.lettuce,
            'onion': self.onion,
            'cheese': self.cheese,
            'bun': self.bun,
            'meat': self.meat,
            'bacon': self.bacon,
            'mockMeat': self.mockMeat,
            'cucumber': self.cucumber,
            'chicken': self.chicken,
            'jalapeno': self.jalapeno
        }

    def __repr__(self):
        return (
            f'<Order(id={self.id}, burgerName="{self.burgerName}", '
            f'tomato={self.tomato}, lettuce={self.lettuce}, onion={self.onion}, '
            f'cheese={self.cheese}, bun="{self.bun}", meat="{self.meat}", '
            f'bacon={self.bacon}, mockMeat={self.mockMeat}, cucumber={self.cucumber}, '
            f'chicken={self.chicken}, jalapeno={self.jalapeno})>'
        )