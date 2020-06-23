import numpy as np
from flask import Flask, request, jsonify, render_template
from flask import Flask, render_template, request
import pickle


# Loading the Multinomial Naive Bayes model and CountVectorizer object 
filename = 'model.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('cv-model.pkl','rb'))
app = Flask(__name__)


@app.route('/')
def home():
	return render_template('form.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect)
        return render_template('form.html', prediction=my_prediction)
if __name__ == '__main__':
	app.run(debug=True)

