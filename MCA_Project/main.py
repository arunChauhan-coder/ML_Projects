
# importing libraries
from flask import Flask,request,render_template,redirect
import joblib
import warnings
warnings.filterwarnings("ignore")

# intializing flask
app = Flask(__name__)

# Loading Models
heart = joblib.load('heart_model.pkl')
sc_heart = joblib.load('sc_heart.pkl')

# Handling get request at home route
@app.route('/')
def home():
    return render_template('index.html')

# Handling post request on home route
@app.route('/',methods = ['post'])

def home_1():

    # Fetching input from webpage

    Age = request.form.get('Age')
    Sex = request.form.get('Sex')
    CP = request.form.get('CP')
    Trest = request.form.get('Trest')
    Chol = request.form.get('Chol')
    Fbs = request.form.get('Fbs')
    Rest = request.form.get('Rest')
    Thalach = request.form.get('Thalach')
    Exang = request.form.get('Exang')
    OP = request.form.get('OP')
    Slope = request.form.get('Slope')
    CA = request.form.get('CA')
    Thal = request.form.get('Thal')
    sex1 = 0
    Sex = Sex.lower()


    if Sex == "male":
        sex1 = 1

    input = [Age, sex1, CP, Trest, Chol, Fbs, Rest, Thalach, Exang, OP, Slope, CA, Thal]

    # PreProcessing

    # Feature Scaling
    data = sc_heart.transform([input])
    result = heart.predict(data)

    # Prediction
    if result[0] == 1:
        return render_template('Positive.html')
    else:
        return render_template('Negative.html')

# Defining Back Button Route
# It will redirect to home page
@app.route('/back',methods = ['post'])
def back():
    return redirect('/')



app.run(port=7007)
