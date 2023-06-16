from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    


    else:
        data=CustomData(
            fueltype=float(request.form.get('fueltype')),
            aspiration = float(request.form.get('aspiration')),
            carbody = float(request.form.get('carbody')),
            drivewheel = float(request.form.get('drivewheel')),
            wheelbase = float(request.form.get('wheelbase')),
            carlength = float(request.form.get('carlength')),
            carwidth = request.form.get('carwidth'),
            carheight= request.form.get('carheight'),
            curbweight = request.form.get('curbweight'),
            enginetype = request.form.get('enginetype'),
            cylindernumber = request.form.get('cylindernumber'),
            enginesize = request.form.get('enginesize'),
            fuelsystem = request.form.get('fuelsystem'),
            boreratio = request.form.get('boreratio'),
            stroke = request.form.get('stroke'),
            compressionratio = request.form.get('compressionratio'),
            horsepower = request.form.get('horsepower'),
            peakrpm = request.form.get('peakrpm'),
            citympg = request.form.get('citympg'),
            highwaympg = request.form.get('highwaympg'),
        
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('results.html',final_result=results)






if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
