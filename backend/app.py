from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from db_interface import DBInterface, Product

db_instance = DBInterface()
db_instance.Seed()

app = Flask(__name__, static_folder="../react-demo/dist", static_url_path="/")
CORS(app) 

@app.route('/')
def index():
    return send_from_directory(app.static_folder, "index.html")

# Optional: for React Router support (serves index.html for any unknown path)
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, "index.html")

# API
@app.get('/api/product')
def product_get():
    p_list = db_instance.Read()
    return jsonify(p_list), 200

@app.post('/api/product')
def product_post():    
    p = db_instance.Create(
        name= request.json['name'],
        price= request.json['price'],
        stock= request.json['stock'],
        description= request.json['description'])
    return jsonify(p), 201

@app.get('/api/product/<int:id>')
def product_id_get(id):
    p = db_instance.Read_ID(id)
    return jsonify(p), 200

@app.put('/api/product/<int:id>')
def product_put(id):
    p = Product(
        id= id,
        name= request.json['name'],
        price= request.json['price'],
        stock= request.json['stock'],
        description= request.json['description']
    )
    p = db_instance.Update(p)
    return jsonify(p), 201

@app.delete('/api/product/<int:id>')
def product_delete(id):
    status = db_instance.Delete(id)
    return {"deleted": status}, 200


# Running app
if __name__ == '__main__':
    app.run(debug=True)