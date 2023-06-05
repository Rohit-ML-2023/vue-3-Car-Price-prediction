from flask import Flask   , jsonify, request
import pickle

from flask_cors import CORS, cross_origin

import numpy as np
# pip install -U flask-cors 
# # # initialize our Flask application
app = Flask(__name__)
app.config['ENV']="development"

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

model = pickle.load(open('car_dekho.pickle', 'rb'))


@app.route("/")
@cross_origin()
def hello_world():
    return "Hello,-world!"



@app.route("/model", methods=["GET"])
def predwine():

    if request.method == 'GET':
        
        try:
            # a = float(request.args.get('alcohol'))
            a = request.args.get('Car_Name')
            b = request.args.get('Car_Model')
            c = request.args.get('Kms_Driven')
            d = request.args.get('No_of_Years')
            e = request.args.get('Fuel_Type')
            f = request.args.get('Transmission')
            g = request.args.get('Owner')
            try:
                    h = int(d)**2
                    i = int(c)**2

            except:
               h= 1
               i= 1
           
        except:
            # x= 1
            a = 1
            b = 1
            c = 1 
            d = 1
            e = 1
            f = 1
            g = 1
            h = 1 
            i= 1
            h = float(request.args.get('No_of_Years'**2))
            i = float(request.args.get('Kms_Driven'**2))
    

        final_features = ([[a, b, c, d, e, f, g,h,i]])
        # final_features = [[1,45,100.00,6,36,10000,1,0,0,1,1,0,0,0,0]]

        prediction = model.predict(final_features)
        print(prediction)

    return jsonify(str("Class  " + str(prediction[0])))


#  main thread of execution to start the server
if __name__ == '__main__':
    app.run(debug=True)
  