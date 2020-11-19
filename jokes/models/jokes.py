from ..utils.database import db
from marshmallow_sqlalchemy import SQLAlchemySchema,auto_field
from marshmallow import fields

class Joke(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(255),nullable=False)
    content=db.Column(db.Text(),nullable=False)


    def __init__(self,name,content):
        self.name=name
        self.content=content

    def __repr__(self):
        return f"{self.name} says {self.content}"
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class JokeSchema(SQLAlchemySchema):
    class Meta:
        model=Joke
        load_instance=True


    id=auto_field()
    name=auto_field()
    content=auto_field()