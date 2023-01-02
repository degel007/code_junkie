#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import tui
import csv
import pandas as pd
import numpy as np



#Option 5
#Define a function that returns the names for all the transaction 
def query_by_alpha():
    tui.started('Retrieve carnames alphabetically')
    df_car_sales = pd.read_csv("Car_Price.csv") 
    CarName = df_car_sales.CarName
#We sort the values alphabetically
    print(CarName.sort_values())
    tui.completed()

    
#Option 6
#Define a function that displays the total price of cars sold by carbody type
def total_sales_by_carbody():
    tui.started('Retrieve summary of sales (total car price) for each car body')
    df_car_sales = pd.read_csv("Car_Price.csv") 
#Get a new dataframe from the dataset having two columns 'price' and 'carbody'
    car_price_per_body = df_car_sales[['price', 'carbody']]
#Grouping the elements in the price column based on carbody type using the .groupby() function 
    by_body = car_price_per_body.groupby(['carbody'])
    
#Convert the carbody column to an array of distinct elements
    bodies = np.unique([car_price_per_body['carbody']])
#Taking an input from the user indicating the specific carbody type they wish to query    
#Looping through the array to provide a condition by which the user's entry is valid, ensuring the entry is... 
#converted to lowercase to march a text in the array
    cb = input('Enter car body: ')
    if cb.lower() not in bodies:
        print('Invalid selection! Choose a carbody in the dataset.')
    else:
        exact_body = by_body.get_group(cb.lower())
#We sum up the prices of of the cars under selected carbodytypes
        total_sales_per_body = "${:,}".format(sum(exact_body.price))
        print(f'The total sales for {cb.lower()} cars is {total_sales_per_body}')
    tui.completed()
    

    
#Option 7
#Define a function that displays the prices of cars bought by a selected carbody
def price_per_carbody():
    tui.started('Retrieve the top 5 car sale by price (the most expensive) and per car body')
    df_car_sales = pd.read_csv("Car_Price.csv")
#Get a new dataframe from the dataset having three columns - 'Carname', 'price' and 'carbody'
    car_body_price = df_car_sales[['CarName','price', 'carbody']]
    by_body = car_body_price.groupby(['carbody'])
    cb = input('Enter car body: ')
#Convert the carbody column to an array of distinct elements
    bodies = np.unique([car_body_price['carbody']])
#Looping through the array to provide a condition by which the user's entry is valid, ensuring the entry is... 
#converted to lowercase to march the text in the array
    
    if cb.lower() not in bodies:
        print('Invalid selection! Choose a carbody in the dataset.')
    else:
        exact_body = by_body.get_group(cb.lower())
        exact_body_sorted = exact_body.sort_values('price', ascending = False)
        print(exact_body_sorted[0:5])
    tui.completed()
    
    
#Option 8
#To retrieve the highway mileage of all cars,arranged in descending order    
def get_highway_mileage():
    tui.started('Retrieve the highway mileage of all cars,arranged in descending order')
    df_car_sales = pd.read_csv("Car_Price.csv")
    highway_table = df_car_sales[['CarName', 'highwaympg']]
#Sorting the 'highwaympg' column in descending order
    mileage_cars = highway_table.sort_values('highwaympg', ascending = False)
    print(mileage_cars)
    tui.completed()


