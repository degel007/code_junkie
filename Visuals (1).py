#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import tui
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Option 9
#Define a function that shows a barchart visualization of the number of cars sold based on fuelsystems
def cs_visuals_1():
    tui.started('Visualize the number of cars per fuel system using a bar chart')
    df_car_sales = pd.read_csv("Car_Price.csv") 
    car_per_fs = df_car_sales[['CarName','fuelsystem']]
    fs =np.array(car_per_fs['fuelsystem'])
#We convert the fuelsystem column into an array with unique elements and assign x and y axis for a bar chart using indexing
    fs_element = np.unique(fs, return_counts = True)
    Fuel_system = fs_element[0]
    Number_of_cars_per_fs = fs_element[1]
    
    plt.figure(figsize=(12, 9))
    plt.title('Car Sold by Fuel System', fontsize = 18)
    plt.xlabel('Fuel Systems', fontsize = 12)
    plt.ylabel('Number of Cars Sold', fontsize = 12)
    
    plt.bar(Fuel_system, Number_of_cars_per_fs)
    plt.show()
    tui.completed()

    
    
# Option 10
 #Define a function that displays a barchart subplots showing the horsepower of the five most expensive cars sold
def cs_visuals_2():
    tui.started('Visualize the horsepower of the top 5 car sale by price (the cheapest) using a subplot')
    df_car_sales = pd.read_csv("Car_Price.csv")
    hp_price = df_car_sales[['CarName', 'horsepower', 'price']]
#Sorting values in ascending order and restricting operation to only the top five rows of the dataframe
    top_5_sales = hp_price.sort_values(ascending = True, by = 'price')[0:5]
    print(top_5_sales)
    fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(1,5,figsize=(20,7))
    
#Assigning x and y axis to the subplots using the .loc function on the dataframe, indicating colour and title
    
    ax1.bar(top_5_sales['CarName'].loc[138], top_5_sales['horsepower'].loc[138], color = 'black')
    ax1.set(title = 'SUBARU HORSEPOWER')
    
    ax2.bar(top_5_sales['CarName'].loc[18], top_5_sales['horsepower'].loc[18], color = 'purple')
    ax2.set(title = 'CHEVROLET IMPALA HORSEPOWER')
    
    ax3.bar(top_5_sales['CarName'].loc[50], top_5_sales['horsepower'].loc[50], color = 'green')
    ax3.set(title = 'MAXDA RX3 HORSEPOWER')
    
    ax4.bar(top_5_sales['CarName'].loc[150], top_5_sales['horsepower'].loc[150], color = 'orange')
    ax4.set(title = 'TOYOTA CORONA MARK ii HORSEPOWER')
    
    ax5.bar(top_5_sales['CarName'].loc[76], top_5_sales['horsepower'].loc[76], color = 'indigo')
    ax5.set(title = 'MISTUBISHI MIRAGE HORSEPOWER')
    
    plt.show()
    tui.completed()
    

    
    
    #Option 11
# We define a function that displays the percentage of the number of cars sold  by carbody
def sales_percentage_by_carbody():
    tui.started('Visualize the percentage of the number of cars sold  by carbody in a pie chart')
    df_car_sales = pd.read_csv("Car_Price.csv")
    
#We convert the carbody column into an array with unique elements and assign properties for the piechart using indexing
    each_car_type = np.unique(([df_car_sales.carbody]), return_counts = True)
    carbody = each_car_type[0]
    carbody_count = each_car_type[1]
    
    plt.figure(figsize = (10,9))
    wedgeprops = {"linewidth": 2, 'width':1, "edgecolor":"k"} # Width = 1
    explode = [0.4, 0.1, 0.1, 0.1, 0.1]
    plt.pie(carbody_count, 
            labels = carbody, 
            autopct='%1.1f%%', 
            pctdistance = 0.6,
            radius = 1, 
            wedgeprops = wedgeprops, 
            explode = explode
        )
    plt.legend(carbody, loc = 'upper right', fontsize = 15)
    

    plt.show()
    
    tui.completed()
    


