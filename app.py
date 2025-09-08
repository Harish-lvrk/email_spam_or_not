# Import the Flask class from the flask module
from flask import Flask, render_template, request, jsonify
from utility import model_predict
# Create an instance of the Flask class
app = Flask(__name__)

# Load models

# Home route
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    email = request.form.get('email')
    
    prediction = model_predict(email)  # get single value
    
    return render_template("index.html", prediction=prediction, email=email)

@app.route('/api/predict', methods =['POST'])
def predict_api():
    data = request.get_json(force = True) # Get data postea as json
    email = data['content']

    prediction = model_predict(email)

    if prediction == 1:
        prediction = "spam"
    else:
        prediction ="Not spam"
    
    return jsonify({
        'prediction' : prediction,
        'email' : email
    })


# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
