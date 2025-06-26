from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs from the form
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
    except ValueError:
        return render_template('index.html', prediction_text="⚠️ Please enter valid numeric values.")

    # Prepare input for prediction
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)

    # Map numerical prediction to flower species
    species_map = {0: 'Setosa 🌸', 1: 'Versicolor 🌺', 2: 'Virginica 🌼'}
    result = species_map.get(prediction[0], "Unknown")

    return render_template('index.html', prediction_text=f'Predicted Iris Species: {result}')

if __name__ == "__main__":
    app.run(debug=True)
