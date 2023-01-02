
import tui
import csv
import pandas as pd
import numpy as np



#Option 1
# We define a function to help the user retrieve all information of specific transactions by Car ID.
def retrieve_by_card_ID():
    tui.started('Retrieve a record for an individual car by ID')
    df_car_sales = pd.read_csv("Car_Price.csv")
# Considering the uniqueness of elements in the Car_ID column, we make the column the index of the dataset
    df_car_sales.index = df_car_sales['car_ID']
# We use a try and except loop to limit operation to integers alone, with an except 'ValueError'
    try:
        car_ID = int(input('Enter Car ID number: '))
# Provide conditions within which the user's entry is valid and prompt to enter a new number when entry is outside range 
        while car_ID > 205 or car_ID < 1:
            print('Invalid selection. Number not in range, must be within range 1 to 205. Try again')
            car_ID = int(input('Enter Car ID number: '))
        else:
            row = df_car_sales.loc[car_ID]
            print([[row]])
    except ValueError:
        print('Invalid selection. Car ID must be a NUMBER between 1 and 205')
    tui.completed()
    

    
#Option 2
# We define a function that displays all the cars for a given cylinder number
def cars_by_cylindernumber():
    tui.started('Retrieve all cars for a specified Cylinder Number')
    df_car_sales = pd.read_csv("Car_Price.csv")
# We create a new dataframe of two columns 'Carname' and 'cylindernumber'
    cs1 = df_car_sales[['CarName', 'cylindernumber']]
# We use a try and except loop to limit operation to integers alone, with an except 'ValueError'
    try:
        cn = int(input('Enter Cylinder Number: '))
# Provide conditions within which the user's entry is valid and prompt to enter a new number when entry is outside range
        while cn > 6 or cn < 2:
            print('Invalid selection. Cylinder number must be within number range 2 to 6')
            cn = int(input('Enter Cylinder Number: '))
        else:
            exact_cn = cs1[cs1['cylindernumber']==cn]
            print(exact_cn)
    except ValueError:
        print('Invalid Selection. Cylinder number is a number between 2 and 6')
    tui.completed()
    

    
#Option 3
#Define a function that displays all the cars for a selected carbodytype
def name_by_carbody():
    tui.started('Retrieve all cars by the specified Car Body')
    df_car_sales = pd.read_csv("Car_Price.csv")
# We create a new dataframe of two columns 'Carname' and 'carbody'
    cs2 = df_car_sales[['CarName', 'carbody']]
#Prompt an input of a carnody type from the user
    cb2 = input('Enter Car bodytype: ')
#Convert the carbody column to an array of distinct elements
    bodies = np.unique([cs2['carbody']])
#Looping through the array to provide a condition by which the user's entry is valid, ensuring the entry is... 
#converted to lowercase to march the text in the array
    if cb2.lower() not in bodies:
        print('Invalid selection! Choose a carbody in the dataset.')
    else:
        exact_cb = cs2[cs2['carbody']==cb2.lower()]
        print(exact_cb)

    tui.completed()

 

    
#Option 4
#Define a function that displays four details for a selected transaction - Carname, cylindernumber, doornumber and carbody
def retrieve_4col_by_id():
    tui.started('Specifications by ID, showing Car Name, Cylinder Number, Door Number, and Car body')
    df_car_sales = pd.read_csv("Car_Price.csv")
# Considering the uniqueness of elements in the Car_ID column, we make the column the index of the dataframe
    df_car_sales.index = df_car_sales['car_ID']
# We get a new dataframe for the four columns we wish to query and request input from the user
    cs3 = df_car_sales[['CarName','cylindernumber', 'doornumber', 'carbody']]
    try:
        car_ID = int(input('Enter Car ID number: '))
# Provide conditions within which the user's entry is valid and prompt to enter a new number when entry is outside range 
        while car_ID > 205 or car_ID < 1:
            print('Invalid selection. Number not in range, must be within range 1 to 205. Try again')
            car_ID = int(input('Enter Car ID number: '))
        else:
#We retrieve the information by accessing the row of the dataframe by the input of the user
            result = cs3[car_ID - 1: car_ID]
            print(result)
    except ValueError:
        print('Invalid selection. Car ID must be a NUMBER between 1 and 205')
    tui.completed()





 
    
    
    
  
        
        

