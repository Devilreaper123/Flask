from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT,jwt_required

from security import authenticate, identity
app = Flask(__name__)
app.secret_key = 'ronit'
api = Api(app)
items = []
jwt = JWT(app , authenticate , identity) # Creates a new endpoint named /auth

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {"Item": item}, 200 if item else 404

    def post(self, name):
        # force=True(Converts the data into json, does not look for the content type) , silent=True (Does not give error just return none )
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {"Message": f"An item with the name '{name}' already exist"}, 400
        data = request.get_json()
        item = {"name": name, "price": data['price']}
        items.append(item)
        return {'item': item}, 201
        # return {"Message": "Item not found"}, 404


class ItemList(Resource):
    def get(self):
        return {"Item": items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=4000, debug=True)
