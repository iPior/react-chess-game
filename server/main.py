from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
cors = CORS(app, origins="*")

@app.route('/api/claude', methods=['GET'])
def claude():
  return jsonify(
    {
      'message': 'Hello, Claude!'
      }
  )


if __name__ == '__main__':
  app.run(debug=True, port=8080)