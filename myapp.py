from flask import Flask,render_template,request
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle
app = Flask(__name__)


@app.route('/')
def hello_world():
   return render_template('index.html')


@app.route('/predict',methods=['POST'])
def get_result():
	poly = pickle.load(open('poly.pkl','rb'))
	model = pickle.load(open('model.pkl','rb'))
	query = [[float(request.form['text2'])]]
	x_query = poly.transform(query)
	sal = model.predict(x_query)
	return 'Dear '+ request.form['text1'] +'Your prediction salary after '+request.form['text2']+'Experience is : '+str(sal)
	
if __name__ == '__main__':
   app.run(debug=True)




 # """
	# model pkl
	# poly.pkl
	# myapp.py
	# templates/index.html
	# requirements.txt
	# profile

 # """
