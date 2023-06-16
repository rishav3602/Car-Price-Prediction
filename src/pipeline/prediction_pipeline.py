import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(self,
                 fueltype:str,
                 aspiration:str,
                 carlength:float,
                 carbody:str,
                 drivewheel:str,
                 wheelbase:float,
                 carwidth:float,
                 carheight:float,
                 curbweight:float,
                 enginetype:str,
                 cylindernumber:float,
                 enginesize:float,
                 fuelsystem:str,
                 boreratio:float,
                 stroke:float,
                 horsepower:float,
                 compressionratio:float,
                 peakrpm:float,
                 citympg:float,
                 highwaympg:float,
                 
                 ):
        
        self.fueltype=fueltype
        self.aspiration=aspiration
        self.carlength=carlength
        self.carbody=carbody
        self.drivewheel=drivewheel
        self.wheelbase=wheelbase
        self.carwidth = carwidth
        self.carheight = carheight
        self.curbweight = curbweight
        self.enginetype = enginetype
        self.cylindernumber = cylindernumber
        self.enginesize = enginesize
        self.fuelsystem = fuelsystem
        self.boreratio = boreratio
        self.stroke = stroke
        self.horsepower = horsepower
        self.compressionratio = compressionratio
        self.peakrpm = peakrpm
        self.citympg = citympg
        self.highwaympg = highwaympg
        

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'fueltype':[self.fueltype],
                'aspiration':[self.aspiration],
                'carlength':[self.carlength],
                'carbody':[self.carbody],
                'drivewheel':[self.drivewheel],
                'wheelbase':[self.wheelbase],
                'carwidth':[self.carwidth],
                'carheight':[self.carheight],
                'curbweight':[self.curbweight],
                'enginetype':[self.enginetype],
                'fuelsystem':[self.fuelsystem],
                'boreratio':[self.boreratio],
                'stroke':[self.stroke],
                'horsepower':[self.horsepower],
                'compressionratio':[self.compressionratio],
                'peakrpm':[self.peakrpm],
                'citympg':[self.citympg],
                'highwaympg':[self.highwaympg],
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)