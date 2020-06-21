import numpy as np
from flask import Flask, request, jsonify, render_template
# Importing essential libraries
from flask import Flask, render_template, request
import pickle
#import re
#import nltk
#from nltk.corpus import stopwords
#from nltk.stem.porter import PorterStemmer
#from sklearn.feature_extraction.text import CountVectorizer

# Load the Multinomial Naive Bayes model and CountVectorizer object from disk
filename = 'model.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('cv-model.pkl','rb'))
#ps = PorterStemmer()

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

