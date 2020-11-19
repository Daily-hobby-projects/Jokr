from ..utils.database import db
from marshmallow_sqlalchemy import ModelSchema
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


class JokeSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model=Joke
        sqla_session=db.session

    id=fields.Integer()
    name=fields.String()
    content=fields.String()
