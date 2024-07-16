## Used Car Price Predictor - Web App with Machine Learning

This repository contains the code for a web application that predicts used car prices based on user input. 

**Key Features:**

* **Machine Learning Model:** Leverages a pre-trained Linear Regression model (`LinearRegressionModel.pkl`) to estimate prices.
* **User Interface:** 
    * Interactive form allows users to select car company, model, year, fuel type, and odometer reading.
    * Displays the predicted price in a user-friendly format.
* **Flask Framework:** Built using Flask, a lightweight web framework for Python.
* **Bootstrap Integration:** Utilizes Bootstrap for responsive design and a clean user interface.

**Project Structure:**

* `app.py`: Contains the Flask application logic, including routing, data loading, prediction functionality, and form handling.
* `Final_dataset.csv`: The dataset used to train the machine learning model.
* `LinearRegressionModel.pkl`: The pickled machine learning model file.
* `templates/index.html`: The HTML template for the web application's user interface.
* `static/css/main.css` : Custom styles for the web app.

**Instructions:**

1. Ensure you have Python, Flask, and other dependencies installed.
2. Place the `Final_dataset.csv` and `LinearRegressionModel.pkl` files in the same directory as `app.py`.
3. Run the application using `flask run`.
4. Access the web app in your browser at `http://127.0.0.1:5000/` (or `localhost:5000/`).

**Further Enhancements:**

* Integrate with a car data API to dynamically populate car models based on the selected company.
* Deploy the application to a web hosting platform for wider accessibility.
* Explore more advanced machine learning models for potentially better prediction accuracy.

