from flask import Flask , request
from flask_restful import Resource, Api , reqparse

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be blank")
    parser.add_argument('title', type=str, required=True, help="This field cannot be blank")
    parser.add_argument('amount', type=int, required=True, help="This field cannot be blank")

    def get(self, _id, name):
        items = next(filter(lambda x: x['title'] == title, items), None)
        if items:
            return {'items' : items, }, 200
        return {'Error': "No one items found in store back"}, 403


    def get(self, _id, name):
        item = next(filter(lambda x: x['title'] == title, x['id'] == _id, items), None)
        if item:
            return {'item' : item, 'id' : _id}, 200
        return {'Error': "Item with that id not found"}, 404

    def post(self, _id, title)
        if next(filter(lambda x: x['title'] == title, _id, items), None):
            return {'Error' : 'Item with this id already exists'.format(title)}, 400
        request_body = Item.parser.parse_args()
        item = {'title' : title, 'price' : request_body['price'], 'amount': request_body['amount']}
        items.append(item)
        return item, 201
        print('Message': 'Item created')
        
    def put(self, _id, name):
        item = next(filter(lambda x: x['id'] == _id, items), None)
        if item:
            data = Item.parser.parse_args()
            item.update(data)
            return item, 202 
        return {"Error" : "Item with this id not found}, 404


    def delete(self, name):
        global items 
        start_len = len(items)
        items =  list(filter(lambda x: x['id'] != _id, items))
        if abs(len(items) - start_len) > 0:
            return {'Message' : 'Item deleted'}, 202
        return {'Error' : 'Item with that name not found'}, 404
        
class ItemCollection(Resource):
    def get(self):
        return {'items' : items }, 200
 
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemCollection, "/items")



if __name__ == "__main__":
    app.run(port=8080, debug=True)
