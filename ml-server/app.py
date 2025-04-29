from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([[data['attendance'], data['avg_score'], data['income_score']]])
    risk_score = model.predict_proba(features)[0][1]
    
    if risk_score > 0.7:
        risk_level = 'High'
    elif risk_score > 0.4:
        risk_level = 'Medium'
    else:
        risk_level = 'Low'
        
    return jsonify({'risk_score': float(risk_score), 'risk_level': risk_level})

if __name__ == '__main__':
    app.run(port=5000)
