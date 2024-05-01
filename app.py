from flask import Flask, request, jsonify, request

app = Flask(__name__)


# This route will receive data from the website
@app.route('/temperature', methods=['POST'])
def receive_data():
    data = request.json

    # Extracting the temperature data
    temperature = data.get('temperature')

    print("Data modtaget", temperature)

    # You can now use the temperature data as needed

    # Dummy response just for demonstration
    response = {'message': 'Data received successfully'}

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
