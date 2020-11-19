from flask import Flask,request,redirect,jsonify,make_response,Blueprint
from ..models.jokes import Joke , JokeSchema

api_bp=Blueprint('api',__name__)


@api_bp.route('/',methods=['POST'])
def create_joke():

    data=request.get_json()

    new_joke=Joke(name=data['name'],content=data['content'])

    new_joke.save()

    joke_schema=JokeSchema()
    joke=joke_schema.dump(new_joke)


    return make_response(jsonify(
        {"message":"Joke added",
        "success":True,
        "joke":{
            "name":data['name'],
            "content":data["content"]
        }
    }
    ),201)


@api_bp.route('/delete/<joke>',methods=['DELETE'])
def delete_joke(joke):

    joke_to_delete=Joke.query.filter_by(content=joke).first()

    joke_to_delete.delete()


    return redirect(url_for('api.index'))