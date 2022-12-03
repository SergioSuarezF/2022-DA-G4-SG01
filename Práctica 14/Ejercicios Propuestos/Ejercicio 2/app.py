import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

# USAR KEY PROPIA
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('users')

@app.route('/users', methods=['POST'])
def create():
    try:
        id = request.json['doc']
        todo_ref.document(id).set(request.json)
        return jsonify({"message": 'Documento creado'}), 200
    except Exception as e:
        return f"error: {e}"

@app.route('/users', methods=['GET'])
def read():
    try:
        todo_id = request.args.get('doc')
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in todo_ref.stream()]
            return jsonify(all_todos), 200
    except Exception as e:
        return f"error: {e}"

@app.route('/users', methods=['PUT'])
def update():
    try:
        id = request.json['doc']
        todo_ref.document(id).update(request.json)
        return jsonify({"message": 'Documento actualizado'}), 200
    except Exception as e:
        return f"error: {e}"

@app.route('/users', methods=['DELETE'])
def delete():
    try:
        todo_id = request.args.get('doc')
        todo_ref.document(todo_id).delete()
        return jsonify({"message": 'Documento eliminado'}), 200
    except Exception as e:
        return f"error: {e}"

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)