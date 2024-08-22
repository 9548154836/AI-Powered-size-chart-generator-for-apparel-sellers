# app.py

from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the clustered data
data = pd.read_csv('data/clustered_data.csv')

@app.route('/get_size_chart', methods=['GET'])
def get_size_chart():
    # Extract parameters from request
    height = request.args.get('height', type=float)
    weight = request.args.get('weight', type=float)
    chest = request.args.get('chest', type=float)
    waist = request.args.get('waist', type=float)
    hip = request.args.get('hip', type=float)
    
    # Filter the data to find the closest match
    filtered_data = data[
        (data['height'] == height) & 
        (data['weight'] == weight) & 
        (data['chest'] == chest) & 
        (data['waist'] == waist) & 
        (data['hip'] == hip)
    ]
    
    if not filtered_data.empty:
        size_chart = filtered_data[['brand', 'size']].to_dict(orient='records')
        return jsonify({'status': 'success', 'size_chart': size_chart})
    else:
        return jsonify({'status': 'error', 'message': 'No matching size found'}), 404

if __name__ == '_main_':
    app.run(debug=True)
