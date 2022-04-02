from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        print("POST Result : ",result)
        return jsonify(str(result))
    else:
        a = int(request.args.get('num1'))
        b = int(request.args.get('num2'))
        result = a + b
        print("GET Result ",result)
        return jsonify(str(result))


if __name__ == '__main__':
    app.run()
