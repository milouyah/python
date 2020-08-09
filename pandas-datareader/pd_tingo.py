import os
import pandas_datareader as pdr
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

df = pdr.get_data_tiingo('AMZN', api_key=config['TIINGO']['TIINGO_API_KEY'])
print(df)
