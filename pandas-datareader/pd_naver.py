import pandas_datareader.data as web
from date import dt

print(dt.now())

samsung='005930'
data_source='naver'
start='2020-07-01'
#end='2020-07-14'
end=dt.now()

# https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#naver-finance-data
df = web.DataReader(samsung, data_source, start, end)
#print(df.head())
print(df)

'''
             Open   High    Low  Close    Volume
Date
2019-09-10  47100  47200  46550  47000   9231792
'''