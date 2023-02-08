import pandas as pd
import numpy as np

# Asks user input to select the file and location 
location = input("CSV Location: ")
file_name = input("File name: ")    # In this case it is 'data.csv'

file = location + "/" + file_name

# Pandas functions to prep the file
excelfile = pd.read_csv(file)
df = pd.DataFrame(excelfile)

# Set x and y axes
years = df.iloc[:,0]
population = df.iloc[:,1]

# Plot settings
import matplotlib.pyplot as plt
plt.bar(years, population, width=8)
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Census Numbers: Minneapolis, MN")

# Line of best fit
z = np.polyfit(years, population, 4)
p = np.poly1d(z)
# Add trendline to plot
plt.plot(years, p(years), color="red")

# Prints out the equation of the trendline
print(p)
