from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from db_interface import DBInterface, ProductModel


def create_app():
    db_instance = DBInterface()
    db_instance.Seed()

    app = Flask(__name__, static_folder="../react-demo/dist", static_url_path="/")
    CORS(app) 
    
    @app.route('/')
    def index():
        return send_from_directory(app.static_folder, "index.html")

    @app.errorhandler(404)
    def not_found(e):
        return send_from_directory(app.static_folder, "index.html")

    # API
    @app.get('/api/product')
    def product_get():
        payload = db_instance.Read()  
        if len(payload) == 0:
            return {"error": "Empty table"}, 404  
        return jsonify(payload), 200

    @app.post('/api/product')
    def product_post():    
        p = ProductModel(
            name= request.json['name'],
            price= request.json['price'],
            stock= request.json['stock'],
            description= request.json['description']
        )
        payload = db_instance.Create(p)
        return jsonify(payload), 201

    @app.get('/api/product/<int:id>')
    def product_id_get(id):
        payload = db_instance.Read_ID(id)
        if payload is None:
            return {"error": "Not found"}, 404
        return jsonify(payload), 200

    @app.put('/api/product/<int:id>')
    def product_put(id):
        p = ProductModel(
            id= id,
            name= request.json['name'],
            price= request.json['price'],
            stock= request.json['stock'],
            description= request.json['description']
        )
        payload = db_instance.Update(p)
        return jsonify(payload), 201

    @app.delete('/api/product/<int:id>')
    def product_delete(id):
        status = db_instance.Delete(id)
        return {"deleted": status}, 200

    return app


# Running app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)