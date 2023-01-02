

LINE_WIDTH = 85

def started(msg=""):
    output = f"Operation started: {msg}..."
    dashes = "-" * LINE_WIDTH
    print(f"{dashes}\n{output}\n")

    
def completed():
    dashes = "-" * LINE_WIDTH
    print(f"\nOperation completed.\n{dashes}\n")
    
def error(msg):
    print(f"Error! {msg}\n")

def menu():
    print(f"""Please select one of the following options:
    {"[1]":<10} Retrieve a record for an individual car by ID
    {"[2]":<10} Retrieve all cars for a specified Cylinder Number
    {"[3]":<10} Retrieve all cars by the specified Car Body
    {"[4]":<10} Specifications by ID, showing Car Name, Cylinder Number, Door Number, and Car body
    {"[5]":<10} Retrieve carnames alphabetically
    {"[6]":<10} Retrieve summary of sales (total car price) for each car body
    {"[7]":<10} Retrieve the top 5 car sale by price (the most expensive) and per car body
    {"[8]":<10} Retrieve the highway mileage of all cars,arranged in descending order
    {"[9]":<10} Visualize the number of cars per fuel system using a bar chart
    {"[10]":<10}Visualize the horsepower of the top 5 car sale by price (the cheapest) using a subplot
    {"[11]":<10}Visualize the percentage of the number of cars sold  by carbody in a pie chart
    {"[exit]":<10} Exit Program
    """)
    selection = input("Your selection: ")
    return selection.strip().lower()









    






