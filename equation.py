import pandas as pd
import csv

df = pd.read_csv("products-info.csv")
min_price = df["Unit Price"].min()
max_price = df["Unit Price"].max()
df["Percent Shops"] = df["Percent Shops"]
max_demand = df["Percent Shops"].max()
min_demand = df["Percent Shops"].min()
newPoint = []
normalizedPriceList= []
normalizedDemandList = []

with open("products-info.csv", "r") as file:
    csv_reader=csv.reader(file)
#Basic information
    maxInventory = 50
    minInventory = 0
    priceWeight = 0.50
    inventoryWeight = 0.33
    demandWeight = 0.50
    next(csv_reader)
    for row in csv_reader: 
    #Price, Inventory, and Demand Values based on input
        #inventory = input("What is the inventory of this product")
        price = float(row[2])
        print(price)
        demand = float(row[4])
        #Normalized Values 
        #The more expensive the price, the higher the point value
        normalizedPrice = (price - min_price)/(max_price - min_price)
        #The lower the inventory, the higher the point value
        #normalizedInventory = 1 -(inventory - minInventory)/(maxInventory - minInventory)
        #print("Normalized Inventory: " + str(normalizedInventory))
        #The higher the demand, the higher the point value
        normalizedDemand = (demand - min_demand) / (max_demand - min_demand)

        #Final value calculation - scaled from 1 - 20 points
        value = priceWeight * normalizedPrice + demandWeight * normalizedDemand
        finalValue = round(value * 24 + 1)
        newPoint.append(finalValue)
        normalizedPriceList.append(normalizedPrice)
        normalizedDemandList.append(normalizedDemand)
file.close()
df['Normalized Demand'] = normalizedDemandList
df['Normalized Price'] = normalizedPriceList
df['New Point'] = newPoint
df.to_csv('New Points File.csv', index=False, encoding='utf-8')