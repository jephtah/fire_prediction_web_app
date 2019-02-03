from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators, DecimalField, IntegerField, SubmitField
from keras.models import load_model
# import pickle
# import sqlite3
# import os
import numpy as np

# import HashingVectorizer from local dir
# from vectorizer import vect

app = Flask(__name__)

######## Preparing the Classifier
# cur_dir = os.path.dirname(__file__)
# clf = pickle.load(open(os.path.join(cur_dir,
#                  'model_objects',
#                  'classifier.pkl'), 'rb'))

# json_file = open('model_num.json', 'r')

# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)

# load weights into index model
# loaded_model.load_weights("model_num.h5")
# print("Loaded model from disk")
loaded_model=load_model('./model/fire_ANN.h5')

# db = os.path.join(cur_dir, 'reviews.sqlite')

def classify(input):
    label = {0: 'No Fire', 1: 'Fire'}
    X = np.array([input]).reshape(1,19)
    y = loaded_model.predict_classes(X)

    if y == 0:
      return label[0]
    return label[1]

# def train(document, y):
#     X = vect.transform([document])
#     clf.partial_fit(X, [y])
# def sqlite_entry(path, document, y):
#     conn = sqlite3.connect(path)
#     c = conn.cursor()
#     c.execute("INSERT INTO review_db (review, sentiment, date)"\
#     " VALUES (?, ?, DATETIME('now'))", (document, y))
#     conn.commit()
#     conn.close()

######## Flask
# class ReviewForm(Form):
#     moviereview = TextAreaField('',
#                                 [validators.DataRequired(),
#                                 validators.length(min=15)])

class Fire_Form(Form):
    TempComedor = DecimalField('Enter TempComedor:', default=18.5,validators=[validators.InputRequired(),
                                                              validators.NumberRange(min=10.0, max=30.0)])

    TempHabit = DecimalField('Enter TempHabit:', default=18.5,validators=[validators.InputRequired(),
                                                              validators.NumberRange(min=10.0, max=30.0)]) 

    WeatherTemp = DecimalField('Enter WeatherTemp:', default=18.5, validators=[validators.InputRequired(),
                                                                validators.NumberRange(min=10.0, max=30.0)])    
    
    CO2Comedor = DecimalField('Enter CO2Comedor:', default=18.5, validators=[validators.InputRequired(),
                                                                  validators.NumberRange(min=10.0, max=30.0)])    
    CO2Habit = DecimalField('Enter CO2Habit:',default=18.5, validators=[validators.InputRequired(),
                                                      validators.NumberRange(min=10.0, max=30.0)])                                 
    HumedadComedor = DecimalField('Enter HumedadComedor:', default=18.5, 
                                                      validators=[validators.InputRequired(),validators.NumberRange(min=10.0, max=30.0)])  

    HumedadHabit = DecimalField('Enter HumedadHabit:', default=18.5, validators=  [validators.InputRequired(),
                                                                 validators.NumberRange(min=10.0, max=30.0)])  

    LightingComedor =DecimalField('Enter LightingComedor:', default=18.5,validators=[validators.InputRequired(),
                                                                    validators.NumberRange(min=10.0, max=30.0)])  

    LightingHabit = DecimalField('Enter LightingHabit:', default=18.5,validators=[validators.InputRequired(),
                                                                    validators.NumberRange(min=10.0, max=30.0)])  

    Precipita = DecimalField('Enter Precipita:', default=18.5, validators=[validators.InputRequired(),
                                                               validators.NumberRange(min=10.0, max=30.0)])  

    MeteoExterior = DecimalField('Enter MeteoExterior:', default=18.5, validators=[validators.InputRequired(),
                                                                  validators.NumberRange(min=10.0, max=30.0)])  

    MeteoExterior1 = DecimalField('Enter MeteoExterior1:', default=18.5, validators=[validators.InputRequired(),
                                         validators.NumberRange(min=10.0, max=30.0)])  

    MeteoExterior2 = DecimalField('Enter MeteoExterior2:', default=18.5, validators=[validators.InputRequired(),
                                                            validators.NumberRange(min=10.0, max=30.0)])  

    MeteoExterior3 = DecimalField('Enter MeteoExterior3:', default=18.5, validators=[validators.InputRequired(),
                                                                   validators.NumberRange(min=10.0, max=30.0)])  

    MeteoExterior4 = DecimalField('Enter MeteoExterior4:', default=18.5, validators=[validators.InputRequired(),
                                                                   validators.NumberRange(min=10.0, max=30.0)]) 
    MeteoExteriorPiranometro = DecimalField('Enter MeteoExtPiranometro:', default=18.5,
                             validators=[validators.InputRequired(),
                                         validators.NumberRange(min=10.0, max=30.0)])  


    TemperatureExteriorSensor = DecimalField('Enter TemperatureExteriorSensor:', default=18.5,
                                              validators=[validators.InputRequired(),
                                                validators.NumberRange(min=10.0, max=30.0)])
                               

    HumedadExteriorSensor = DecimalField('Enter HumedadExteriorSensor:', default=18.5,                                     validators= [validators.InputRequired(),
                                          validators.NumberRange(min=10.0, max=30.0)])                                                                            


    DayOfWeek = IntegerField('Enter DayOfWeek:',default= 6,validators=[validators.InputRequired(),                                                      validators.NumberRange(min=1, max=7)])      
                                                                                   

    submit = SubmitField("Enter")

@app.route('/')
def index():
    form = Fire_Form(request.form)
    return render_template('index.html', form=form)

@app.route('/results', methods=['POST'])
def results():
    form = Fire_Form(request.form)
    if request.method == 'POST' and form.validate():
        TempComedor = request.form['TempComedor']
        TempHabit = request.form['TempHabit']
        WeatherTemp = request.form['WeatherTemp']
        CO2Comedor = request.form['CO2Comedor']
        CO2Habit = request.form['CO2Habit']
        HumedadComedor = request.form['HumedadComedor']
        HumedadHabit = request.form['HumedadHabit']
        LightingComedor = request.form['LightingComedor']
        LightingHabit= request.form['LightingHabit']
        Precipita = request.form['Precipita']
        MeteoExterior = request.form['MeteoExterior']
        MeteoExterior1 = request.form['MeteoExterior1']
        MeteoExterior2 = request.form['MeteoExterior2']
        MeteoExterior3 = request.form['MeteoExterior3']
        MeteoExterior4 = request.form['MeteoExterior4']
        MeteoExteriorPiranometro = request.form['MeteoExteriorPiranometro']
        TemperatureExteriorSensor = request.form['TemperatureExteriorSensor']
        HumedadExteriorSensor = request.form['HumedadExteriorSensor']
        DayOfWeek = request.form['DayOfWeek']

        data = [[TempComedor, TempHabit, WeatherTemp, CO2Comedor, CO2Habit, HumedadComedor, HumedadHabit, LightingComedor, LightingHabit, Precipita, MeteoExterior, MeteoExterior1, MeteoExterior2, MeteoExterior3, MeteoExterior4, MeteoExteriorPiranometro,TemperatureExteriorSensor,HumedadExteriorSensor, DayOfWeek]]

        y = classify(data)

        return render_template('results.html', content = data,prediction=y)

    return render_template('index.html', form=form)

# @app.route('/thanks', methods=['POST'])
# def feedback():
#     # feedback = request.form['feedback_button']
#     # review = request.form['review']
#     # prediction = request.form['prediction']

#     # inv_label = {'negative': 0, 'positive': 1}
#     # y = inv_label[prediction]
#     # if feedback == 'Incorrect':
#     #     y = int(not(y))
#     # train(review, y)
#     # sqlite_entry(db, review, y)
#     return render_template('thanks.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
