from flask import Flask,request,redirect,jsonify,make_response,Blueprint
from ..models.jokes import Joke ,JokeSchema

api_bp=Blueprint('api',__name__)


@api_bp.route('/',methods=['POST'])
def create_joke():

    data=request.get_json()

    new_joke=Joke(name=data['name'],content=data['content'])

    new_joke.save()

    joke=JokeSchema().dump(new_joke)

    return make_response(jsonify(
        {"message":"Joke added",
        "success":True,
        "joke":joke
    }
    ),201)


