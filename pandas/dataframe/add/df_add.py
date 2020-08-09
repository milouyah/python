# Append sample
import pandas as pd

'''
[0] List of tupels --> Dataframe
'''
# List of Tuples
students = [ ('jack', 34, 'Sydeny', 'Australia'),
             ('Riti', 30, 'Delhi', 'India' ),
             ('Vikas', 31, 'Mumbai', 'India' ),
             ('Neelu', 32, 'Bangalore', 'India' ),
             ('John', 16, 'New York', 'US'),
             ('Mike', 17, 'las vegas', 'US')  ]

#Create a DataFrame object
dfObj = pd.DataFrame(
    students, 
    columns = ['Name', 'Age', 'City', 'Country'], 
    index=['a', 'b', 'c', 'd', 'e', 'f']) 

print(dfObj)
print('-----------------------------------')
'''
[1] Add row in the dataframe using dataframe.append() and Dictionary
'''

# Pass the row elements as key value pairs to append() function 
modDfObj = dfObj.append(
    {'Name' : 'Sahil' , 'Age' : 22}, 
    ignore_index=True)
print(modDfObj)
print('-----------------------------------')

'''
[2] Add row in the dataframe using dataframe.append() and Series
'''
# Pass a series in append() to append a row in dataframe  
modDfObj = dfObj.append(
    pd.Series(['Raju', 21, 'Bangalore', 'India'], index=dfObj.columns ), 
    ignore_index=True)
print(modDfObj)
print('-----------------------------------')

'''
[3] Add multiple rows in the dataframe using dataframe.append() and Series
'''

# List of series  
listOfSeries = [pd.Series(['Raju', 21, 'Bangalore', 'India'], index=dfObj.columns ) ,
                pd.Series(['Sam', 22, 'Tokyo', 'Japan'], index=dfObj.columns ) ,
                pd.Series(['Rocky', 23, 'Las Vegas', 'US'], index=dfObj.columns ) ]
# Pass a list of series to the append() to add multiple rows
modDfObj = dfObj.append(listOfSeries , ignore_index=True)
print(modDfObj)
print('-----------------------------------')


'''
[4] Add a row from one dataframe to other dataframe using dataframe.append()
'''
# List of Tuples
students = [ ('Rahul', 22, 'Sydeny' , 'Australia') ,
             ('Parul', 23, 'Pune' , 'India')  ]
#Create a DataFrame object
dfObj2 = pd.DataFrame(students, columns = ['Name' , 'Age', 'City' , 'Country'], index=['a', 'b']) 

# add row at index b from dataframe dfObj2 to dataframe dfObj
modDfobj = dfObj.append(dfObj2.loc['b'], ignore_index=True)
print(modDfObj)
print('-----------------------------------')




'''
Add a row from one dataframe to other dataframe using dataframe.append()
'''
# Add a new row at index k with values provided in list
dfObj.loc['k'] = ['Smriti', 26, 'Bangalore', 'India']
print(dfObj)

'''
Add a row in the dataframe at index position using iloc[]
'''
# Add a new row at index position 2 with values provided in list
dfObj.iloc[2] = ['Smriti', 26, 'Bangalore', 'India']
print(dfObj)


# IndexError: single positional indexer is out-of-bounds
# dfObj.iloc[10] = ['Smriti', 26, 'Bangalore', 'India']
# print(dfObj)
