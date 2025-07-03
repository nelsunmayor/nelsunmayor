from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
contractors = []
clients = []
assignments = []

@app.route('/contractors', methods=['GET', 'POST'])
def handle_contractors():
    if request.method == 'POST':
        data = request.json
        contractors.append(data)
        return jsonify({'message': 'Contractor added', 'contractor': data}), 201
    return jsonify(contractors)

@app.route('/clients', methods=['GET', 'POST'])
def handle_clients():
    if request.method == 'POST':
        data = request.json
        clients.append(data)
        return jsonify({'message': 'Client added', 'client': data}), 201
    return jsonify(clients)

@app.route('/assign', methods=['POST'])
def assign_contractor():
    data = request.json
    assignments.append(data)
    return jsonify({'message': 'Assignment created', 'assignment': data}), 201

@app.route('/assignments', methods=['GET'])
def list_assignments():
    return jsonify(assignments)

if __name__ == '__main__':
    app.run(debug=True)
