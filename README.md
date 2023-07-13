# Point Algorithm
The code in this repository will normalize the price and demand values, dependent on the unit price of the items along with their Percent Shops, respectifully. 
Once these values are normalized, they are weighted each at 50% and used to determine a point value from 0 - 25, inclusive. 
The program will also output a new CSV file that contains the new point values.
If needed, one can adjust the weighted values easily. 

In order to work with this file, the user must input a csv file that contains the Product ID,Product Name,Unit Price,Points,Percent Shops in that specific order and name, or else the compiler will raise errors. 

Future adjustments: 
There is currently no data to calculate a normalized inventory value, a variable my team and I thought would be incredibly important to include. 
Once this information is included, this repository will be appropriately updated. 
