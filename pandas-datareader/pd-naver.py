import pandas_datareader.data as web

samsung='005930'
data_source='naver'

# https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#naver-finance-data
df = web.DataReader(samsung, data_source, start='2019-09-10', end='2019-10-09')
print(df.head())

'''
             Open   High    Low  Close    Volume
Date
2019-09-10  47100  47200  46550  47000   9231792
'''