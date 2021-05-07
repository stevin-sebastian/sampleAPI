from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])

def index():
    if(request.method == 'POST'):
        data = request.get_json()
        if('x' or 'y' not in data):
            return jsonify({"Error": "Input Values not defined"}),404
        else:
            sum = int(data['x']) + int(data['y'])
            return jsonify({"Sum": sum}), 200
    elif(request.method == 'GET'):
        return jsonify({"about": "This is an addition Calculator, please define x and y"}), 201


@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'Product' : num*10})
if __name__ == '__main__':
    app.run(debug=True)
