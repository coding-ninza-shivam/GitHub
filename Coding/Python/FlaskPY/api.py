from flask import Flask, jsonify, request
app= Flask(__name__)

# Initial data of my to do list

items=[
    {"id":1,"name":"Item1","description":"This is Item1"},
    {"id":2,"name":"Item2","description":"This is Item2"}
]

@app.route("/")
def home():
    return "Welcome to the sample to do list app"

# get: retrieve all the items
@app.route("/items",methods=["GET"])
def get_items():
    return jsonify(items)

# get: retrieve an item with an ID
@app.route("/items/<int:item_id>",methods=["GET"])
def get_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'item not found'})
    return jsonify(items)

# post: create a new task
@app.route("/items",methods=["POST"])
def create_item():
    if not request.json or not "name" in request.json:
        return jsonify({'error':'item not found'})
    new_item={
        "id":items[-1]['id']+1 if items else 1,
        'name':request.json['name'],
        "description":request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

# put: update an existing item
@app.route("/items/<int:item_id>",methods=["PUT"])
def update_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'item not found'})
    item['name']= request.json.get('name',item["name"])
    item['description']= request.json.get('description',item["description"])
    return jsonify(item)

# delete: delete an existing item
@app.route("/items/<int:item_id>",methods=["DELETE"])
def delete_item(item_id):
    global items
    items=[item for item in items if item['id']!=item_id]
    return jsonify({'result':'item deleted'})

if __name__=="__main__":
    app.run(debug=True)