from flask import Flask, jsonify, request

app = Flask(__name__)

accounts = {"1": {"name": "User One", "email": "user1@example.com"}}

@app.route('/accounts', methods=['GET'])
def list_accounts():
    return jsonify(accounts)

@app.route('/accounts/<id>', methods=['GET'])
def read_account(id):
    return jsonify(accounts.get(id, {"error": "Not found"}))

@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.json
    id = str(len(accounts) + 1)
    accounts[id] = data
    return jsonify({"id": id, "message": "Created"}), 201

@app.route('/accounts/<id>', methods=['PUT'])
def update_account(id):
    accounts[id] = request.json
    return jsonify({"message": "Updated"})

@app.route('/accounts/<id>', methods=['DELETE'])
def delete_account(id):
    if id in accounts:
        del accounts[id]
        return jsonify({"message": "Deleted"})
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
