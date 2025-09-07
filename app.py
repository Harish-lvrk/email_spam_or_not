# Import the Flask class from the flask module
from flask import Flask, render_template, request
import pickle

# Create an instance of the Flask class
app = Flask(__name__)

# Load models
cv = pickle.load(open("models/cv.pkl", "rb"))
clf = pickle.load(open("models/clf.pkl", "rb"))

# Home route
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    email = request.form.get('email')
    tokenized_mail = cv.transform([email])
    prediction = clf.predict(tokenized_mail)[0]  # get single value
    prediction = 1 if prediction == 1 else -1
    return render_template("index.html", prediction=prediction, email=email)

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
