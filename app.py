from flask import Flask, request, jsonify
import serial

app = Flask(__name__)

# Initialize the serial connection to Arduino
# Adjust the port name and baud rate as per the Arduino configuration
ser = serial.Serial('COM3', 9600)  # Example: 'COM3' for Windows, '/dev/ttyUSB0' for Linux


# This route will receive data from the website
@app.route('/send_data', methods=['POST'])
def receive_data():
    # Assuming the data sent from the website is in JSON format
    data = request.json

    # Extract the data you want to send to Arduino
    arduino_data = data.get('arduino_data')  # Adjust as per your JSON structure

    # Convert data to bytes before sending to Arduino
    ser.write(arduino_data.encode())

    # Dummy response just for demonstration
    response = {'message': 'Data sent to Arduino successfully'}

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
